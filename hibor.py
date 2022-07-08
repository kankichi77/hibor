import urllib.request, json, argparse, datetime

PROG_DESC = 'Retrieves and outputs 1-Month HIBOR rates from the HKMA API.\nFORMAT:\nYYYY-MM-DD\tHIBOR_RATE'
BASE_API_URL = 'https://api.hkma.gov.hk/public/market-data-and-statistics'
BASE_API_URL += '/daily-monetary-statistics/daily-figures-interbank-liquidity'
DEFAULT_RECORD_COUNT = 10
MAX_RECORD_COUNT = 1000

def printHiborDataFromApi(
    datefrom = 0,
    dateto = 0,
    recordcount = 0,
    show_date = True
  ):

  if not recordcount or recordcount > MAX_RECORD_COUNT:
    recordcount = DEFAULT_RECORD_COUNT
  
  url = BASE_API_URL + '?fields=end_of_date,hibor_fixing_1m'
  
  if datefrom or dateto:
    if not datefrom: datefrom = dateto
    if not dateto: dateto = datetime.datetime.now().strftime('%Y%m%d')
    datefrom = datetime.datetime.strptime(str(datefrom),'%Y%m%d').strftime('%Y-%m-%d')
    dateto = datetime.datetime.strptime(str(dateto),'%Y%m%d').strftime('%Y-%m-%d')
    url += f'&choose=end_of_date&from={datefrom}&to={dateto}'
    url += f'&sortby=end_of_date&sortorder=asc'
    in_reverse = False
  else:
    in_reverse = True
  url += f'&pagesize={recordcount}'
  #url += '&choose=end_of_date&from=2022-06-01&to=2022-06-30'

  try:
    j = json.loads(urllib.request.urlopen(url).read())
  except Exception as e:
    print(f'ERROR: {e}')
    exit()

  l = j["result"]["records"]
  if in_reverse: l.reverse()

  if j["header"]["success"]:
    if len(l):
      for r in l:
        if show_date: d = f"{r['end_of_date']}\t"
        else: d = ''
        print(f"{d}{r['hibor_fixing_1m']}%")
    else:
      print(f'No data')
  else:
    print(f'ERROR: {j["header"]["err_msg"]}')
  #print(f'{url = }')


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description = PROG_DESC,
    formatter_class=argparse.RawDescriptionHelpFormatter,
  )
  parser.add_argument('-f',
    help = 'The FROM date to retrieve data',
    type = int,
    metavar = 'YYYYMMDD',
    dest = 'datefrom'
    )
  parser.add_argument('-t',
    help = 'The TO date to retrieve data (default: today)',
    type = int,
    metavar = 'YYYYMMDD',
    dest = 'dateto'
    )
  parser.add_argument('-c', '-count',
    help = 'Max number of records to retrieve (default: 10)', 
    type = int,
    metavar = 'N',
    dest = 'recordcount',
    default = DEFAULT_RECORD_COUNT
    )
  parser.add_argument('-nd', '-no_date',
    help = 'Do not display date in output (default: false)',
    action = 'store_false',
    dest = 'no_date'
    )
  args = parser.parse_args()
  
  printHiborDataFromApi(
    datefrom=args.datefrom,
    dateto = args.dateto,
    recordcount = args.recordcount,
    show_date = args.no_date
    )


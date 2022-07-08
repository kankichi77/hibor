import urllib.request, json, datetime

  BASE_API_URL = 'https://api.hkma.gov.hk/public/market-data-and-statistics/daily-monetary-statistics/daily-figures-interbank-liquidity'

def printHiborDataFromApi():
  datefrom, dateto, recordcount = 0, 0, 0
  #datefrom = '2021-11-01'
  #dateto = '2021-11-30'
  recordcount = 10

  url = BASE_API_URL + '?offset=0&fields=end_of_date,hibor_fixing_1m'
  if datefrom and dateto:
    url += f'&choose=end_of_date&from={datefrom}&to={dateto}'
  j = json.loads(urllib.request.urlopen(url).read())
  l = j["result"]["records"]
  if recordcount: l = l[0:recordcount]
  l.reverse()

  for r in l:
    print(f"{r['end_of_date']}\t{r['hibor_fixing_1m']}%")
    #print(f"{r['hibor_fixing_1m']}%")

if __name__ == "__main__":
  printHiborDataFromApi()


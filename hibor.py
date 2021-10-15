import urllib.request
import json
import datetime

today_YYMMDD = datetime.datetime.now().strftime('%y%m%d')
filename = 'hibor_' + today_YYMMDD + '.txt'
f = open(filename, "w")
# url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/er-ir/hk-interbank-ir-daily?segment=hibor.fixing&offset=0&pagesize=10'
url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/daily-monetary-statistics/daily-figures-interbank-liquidity?fields=end_of_date,hibor_fixing_1m&pagesize=1'
r = urllib.request.urlopen(url).read().decode('ascii')
j = json.loads(r)
f.write(json.dumps(j,indent=2))
f.close()
print('Date: {0}'.format(j["result"]["records"][0]["end_of_date"]))
print('1-Month HIBOR Fixing: {0}%'.format(j["result"]["records"][0]["hibor_fixing_1m"]))

# Python HIBOR script
Python script to get the daily 1-month HIBOR rates from the HKMA API
  
HKMA Source:  
https://apidocs.hkma.gov.hk/documentation/market-data-and-statistics/daily-monetary-statistics/daily-figures-interbank-liquidity/

Requirements:
  - Python (ver 3)
  - BeautifulSoup4 (for getting realtime rate from HKAB website)
```
python3 hibor.py -h

usage: hibor.py [-h] [-f YYYYMMDD] [-t YYYYMMDD] [-c N] [-nd]
```
Retrieves and outputs 1-Month HIBOR rates from the HKMA API.  
```  
FORMAT:  
YYYY-MM-DD    HIBOR_RATE

|optional arguments:||
|-------------------|---|
|-h, --help|show this help message and exit|
|-f YYYYMMDD|The FROM date to retrieve data|
|-t YYYYMMDD|The TO date to retrieve data (default: today)|
|-c N, -count N|Max number of records to retrieve (default: 10)|
|-nd, -no_date|Do not display date in output (default: false)|
```
### Create CSV file to open in Excel

```
echo "sep=,">hibor.csv; python3 hibor.py -f 20130620 -c 30 >> hibor.csv
```

### Get today's HIBOR
```
python3 realtime.py
```
Retrieves the 1-month HIBOR from the HKAB website since the rates are published at 11:15am every business day but the API is only updated daily. (to be integrated into hibor.py sometime in the future...)



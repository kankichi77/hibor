Python script to get the daily 1-month HIBOR rates from the HKMA API.

Requirement:
  - Python (ver 3)

% python3 hibor.py -h

usage: hibor.py [-h] [-f YYYYMMDD] [-t YYYYMMDD] [-c N] [-nd]

Retrieves and outputs 1-Month HIBOR rates from the HKMA API.
FORMAT:
YYYY-MM-DD  HIBOR_RATE

optional arguments:
  -h, --help      show this help message and exit
  -f YYYYMMDD     The FROM date to retrieve data
  -t YYYYMMDD     The TO date to retrieve data (default: today)
  -c N, -count N  Max number of records to retrieve (default: 10)
  -nd, -no_date   Do not display date in output (default: false)

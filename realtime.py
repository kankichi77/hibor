import urllib.request, re, datetime
from bs4 import BeautifulSoup

def getRealtimeHIBOR():
    URL = "https://www.hkab.org.hk/en/rates/hibor"
    term, hibor = '', ''
    soup = BeautifulSoup(urllib.request.urlopen(URL), 'html.parser')

    # Get date
    regex_pattern = r'Hong Kong Time on (\d{4}-\d{1,2}-\d{1,2})'
    string_found = re.search(regex_pattern, soup.get_text())
    dt = datetime.datetime.strptime(str(string_found.group(1)),'%Y-%m-%d')

    # Get 1-month HIBOR
    for div in soup.find_all('div', class_="general_table_row"):
        if div.div.div.string == '1 Month':
            term = div.contents[0].div.string
            hibor = div.contents[1].div.string
    if datetime.date.today() == dt.date():
        return {
            "date": dt.strftime('%Y/%m/%d'),
            "term": term,
            "hibor": hibor,
        }
    else:
        return None

if __name__ == "__main__":
    result = getRealtimeHIBOR()
    if result:
        print(f"{datetime.datetime.today():%Y/%m/%d %H:%M}: {result['date']}, {result['hibor']}%")
    else:
        print(f"{datetime.datetime.today():%Y/%m/%d %H:%M}: No new rate published for today.")

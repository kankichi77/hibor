import urllib.request

URL = "https://www.hkab.org.hk/en/rates/hibor"

def getRealtimeHIBOR():
    with urllib.request.urlopen(URL) as f:
        print(f.read().decode('utf-8'))

if __name__ == "__main__":
    getRealtimeHIBOR()

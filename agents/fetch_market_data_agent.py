import os
import requests

API_URL = os.getenv("FREQTRADE_API_URL", "http://127.0.0.1:8080")
USERNAME = os.getenv("FREQTRADE_USERNAME", "Freqtrader")
PASSWORD = os.getenv("FREQTRADE_PASSWORD", "SuperSecret1!")

# Example: Fetch market data for BTC/USDT, 1h timeframe
def fetch_market_data(pair="BTC/USDT", timeframe="1h"):
    url = f"{API_URL}/api/v1/pair/candles"
    params = {"pair": pair, "timeframe": timeframe}
    resp = requests.get(url, params=params, auth=(USERNAME, PASSWORD))
    if resp.ok:
        print(f"Market data for {pair} ({timeframe}):\n", resp.json())
    else:
        print("Failed to fetch market data:", resp.status_code, resp.text)

if __name__ == "__main__":
    fetch_market_data()

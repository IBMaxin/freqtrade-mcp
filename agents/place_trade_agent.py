import os
import requests

API_URL = os.getenv("FREQTRADE_API_URL", "http://127.0.0.1:8080")
USERNAME = os.getenv("FREQTRADE_USERNAME", "Freqtrader")
PASSWORD = os.getenv("FREQTRADE_PASSWORD", "SuperSecret1!")

# Example: Place a buy trade for BTC/USDT with a stake amount of 0.01
def place_trade(pair: str = "BTC/USDT", side: str = "buy", stake_amount: float = 0.01):
    url = f"{API_URL}/api/v1/trade"
    data = {"pair": pair, "side": side, "stake_amount": stake_amount}
    resp = requests.post(url, json=data, auth=(USERNAME, PASSWORD))
    if resp.ok:
        print(f"Trade placed: {resp.json()}")
    else:
        print("Failed to place trade:", resp.status_code, resp.text)

if __name__ == "__main__":
    place_trade()

import os
import requests

API_URL = os.getenv("FREQTRADE_API_URL", "http://127.0.0.1:8080")
USERNAME = os.getenv("FREQTRADE_USERNAME", "freqtrade")
PASSWORD = os.getenv("FREQTRADE_PASSWORD", "12345")

# Scan all strategy files in the given folders and print their names
STRATEGY_FOLDERS = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../strategies')),
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../../user_data/strategies')),
]

def list_strategies():
    strategies = []
    for folder in STRATEGY_FOLDERS:
        if os.path.isdir(folder):
            for fname in os.listdir(folder):
                if fname.endswith('.py') and not fname.startswith('__'):
                    strategies.append(os.path.join(folder, fname))
    return strategies

def main():
    print("Discovered strategy files:")
    for s in list_strategies():
        print(" -", s)
    # Example: fetch bot status
    url = f"{API_URL}/api/v1/status"
    resp = requests.get(url, auth=(USERNAME, PASSWORD))
    if resp.ok:
        print("Bot status:", resp.json())
    else:
        print("Failed to fetch bot status:", resp.status_code, resp.text)

if __name__ == "__main__":
    main()

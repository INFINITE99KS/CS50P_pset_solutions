import requests
import json
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        btc_quote = (requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a072e968ea95bd0db2acc109eff6e65e030e4dd6102b0ebf2860ac6f31fa5734")).json()
        amount = float(sys.argv[1])
        print(f"${amount*float(btc_quote["data"]["priceUsd"]):,.4f}")

    except requests.RequestException:
        sys.exit("API Request error.")
    except ValueError:
        sys.exit("Comman-line argument is not a number")


if __name__ == "__main__":
    main()

import requests
from .models import Contract

def get_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except (requests.RequestException, KeyError):
        return None

def update_prices_for_active_contracts():
    active_contracts = Contract.objects.filter(status=True)
    for contract in active_contracts:
        market_price = get_binance_price(contract.crypto_coin.crypto_symbol)
        if market_price is not None:
            contract.market_price = market_price
            contract.save()

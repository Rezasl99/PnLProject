from django.shortcuts import render
from .models import CryptoCoins, Contract
import requests

def get_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    try:
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except (requests.RequestException, KeyError):
        return None

def home(request):
    crypto_symbol = CryptoCoins.objects.all()

    for crypto in crypto_symbol:
        market_price = get_binance_price(crypto.crypto_symbol)
        if market_price:
            Contract.objects.filter(crypto_coin=crypto).update(market_price=market_price)

    context = {
        'crypto_symbol': crypto_symbol,
    }
    return render(request, 'index.html', context)

from django.shortcuts import render
from .models import CryptoCoins, Contract
import requests
from django.shortcuts import get_object_or_404 , redirect
from .constants import COINS_LIST

def get_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    try:
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except (requests.RequestException, KeyError):
        return None

def home(request):
    """ Displays all the Contracts sorted by coins """
    crypto_symbols = CryptoCoins.objects.all()


    for symbol in crypto_symbols:
        market_price = get_binance_price(symbol.crypto_symbol)
        if market_price:
            Contract.objects.filter(crypto_coin=symbol, status=True).update(market_price=market_price)

    context = {
        'crypto_symbols': crypto_symbols,
    }
    return render(request, 'index.html', context)


def all_contracts(request):
    ''' Displays all the contracts '''
    contracts = Contract.objects.all().order_by('-status')
    for contract in contracts:
        if contract.status == True:
            market_price = get_binance_price(contract.crypto_coin.crypto_symbol)
            contract.market_price = market_price
            contract.save()
    context = {'contracts': contracts}
    return render(request, 'all_contracts.html', context)


def close_contract(request, contract_id):
    '''Closing contract function '''
    contract = get_object_or_404(Contract, id=contract_id)
    contract.status = False
    contract.save()
    return redirect(all_contracts)

def add_contract(request):
    coins_list = COINS_LIST
    if request.method == 'POST':
        crypto_symbol = request.POST.get('crypto_coin', '').upper().strip()
        entry_price = request.POST.get('entry_point')
        leverage = request.POST.get('leverage')
        short_long = request.POST.get('position')

        if short_long == 'False':
            pass
        else:
            is_short = True

        coin_obj, created = CryptoCoins.objects.get_or_create(crypto_symbol=crypto_symbol)


        Contract.objects.create(
            crypto_coin=coin_obj,
            entry_price=entry_price,
            leverage=leverage,
            is_short=is_short,
        )
        return redirect('all_contracts')
    return render(request, 'add_contract.html', {'coins_list': coins_list})
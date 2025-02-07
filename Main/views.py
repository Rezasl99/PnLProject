# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import CryptoCoins, Contract
from .constants import COINS_LIST

def home(request):
    """Displays all the Contracts sorted by coins, without updating prices."""
    crypto_symbols = CryptoCoins.objects.all()
    context = {
        'crypto_symbols': crypto_symbols,
    }
    return render(request, 'index.html', context)

def all_contracts(request):
    """Displays all the contracts, without updating prices."""
    contracts = Contract.objects.all().order_by('-status')
    context = {'contracts': contracts}
    return render(request, 'all_contracts.html', context)

def close_contract(request, contract_id):
    """Closing contract function."""
    contract = get_object_or_404(Contract, id=contract_id)
    contract.status = False
    contract.save()
    return redirect(all_contracts)

def add_contract(request):
    """Adds a new contract."""
    if request.method == 'POST':
        crypto_symbol = request.POST.get('crypto_coin', '').upper().strip()
        entry_price = request.POST.get('entry_point')
        leverage = request.POST.get('leverage')
        short_long = request.POST.get('position')

        is_short = (short_long != 'False')

        coin_obj, created = CryptoCoins.objects.get_or_create(crypto_symbol=crypto_symbol)
        Contract.objects.create(
            crypto_coin=coin_obj,
            entry_price=entry_price,
            leverage=leverage,
            is_short=is_short,
        )
        return redirect('all_contracts')

    return render(request, 'add_contract.html', {'coins_list': COINS_LIST})

from django.shortcuts import render
from .models import CryptoCoins


def home(request):
    crypto_symbol = CryptoCoins.objects.all()

    context = {
        'crypto_symbol': crypto_symbol,
    }
    return render(request, 'index.html', context)

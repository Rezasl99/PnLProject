from django.contrib import admin
from .models import CryptoCoins, Contract

class CryptoCoinsAdmin(admin.ModelAdmin):
    list_display = ('crypto_symbol',)

class ContractAdmin(admin.ModelAdmin):
    list_display = ('crypto_coin', 'entry_price', 'market_price', 'leverage', 'created_at', 'status', 'pnl_percentage')

admin.site.register(CryptoCoins, CryptoCoinsAdmin)
admin.site.register(Contract, ContractAdmin)
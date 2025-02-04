from django.db import models

class CryptoCoins(models.Model):
    crypto_symbol = models.CharField(max_length=20)


    def __str__(self):
        return self.crypto_symbol

class Contract(models.Model):
    crypto_coin = models.ForeignKey(CryptoCoins, on_delete=models.CASCADE, null=True, related_name='contracts')
    entry_price = models.FloatField()
    market_price = models.FloatField()
    leverage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)
    status = models.BooleanField(default= True)


    def __str__(self):
        return f'Entry price {self.entry_price}'

    def pnl_percentage(self):
        return ((self.market_price - self.entry_price) / self.entry_price) * 100 * self.leverage

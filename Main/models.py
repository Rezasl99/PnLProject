from django.db import models

class CryptoCoins(models.Model):
    crypto_symbol = models.CharField(max_length=20)


    def __str__(self):
        return self.crypto_symbol

class Contract(models.Model):
    crypto_coin = models.ForeignKey(CryptoCoins, on_delete=models.CASCADE, null=True, related_name='contracts')
    entry_price = models.FloatField()
    market_price = models.FloatField(null= True, default= 1.0)
    leverage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add= True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default= True)
    is_short = models.BooleanField(default=False)

    def __str__(self):
        return f'Entry price {self.entry_price}'

    def pnl_percentage(self):
        differnce = self.market_price - self.entry_price
        if self.is_short:
            differnce = -differnce
        pnl = (differnce / self.entry_price) * 100 * self.leverage
        return round(pnl, 2)

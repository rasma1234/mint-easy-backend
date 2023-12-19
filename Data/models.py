from django.db import models
class ForexData(models.Model):
    symbol = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    current_price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    percent_change = models.FloatField()

    def __str__(self):
        return f"{self.symbol} - {self.datetime}"

class CryptoData(models.Model):
    symbol = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    current_price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    percent_change = models.FloatField()

    def __str__(self):
        return f"{self.symbol} - {self.datetime}"
    
# class StockData(models.Model):
#     symbol = models.CharField(max_length=10)
#     datetime = models.DateTimeField()
#     current_price = models.FloatField()
#     open_price = models.FloatField()
#     close_price = models.FloatField(null=True)
#     high_price = models.FloatField()
#     low_price = models.FloatField()
#     percent_change = models.FloatField()
#     change = models.FloatField()
#     previous_close = models.FloatField(default=0) 
    
#     def __str__(self):
#         return f"{self.symbol} - {self.datetime}"   
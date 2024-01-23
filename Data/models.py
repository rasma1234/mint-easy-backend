from django.db import models
from django.contrib.auth import get_user_model
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
    
class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    current_price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    percent_change = models.FloatField()
    volume = models.FloatField()
    
    def __str__(self):
        return f"{self.symbol} - {self.datetime}"





class ForexData_15min(models.Model):
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

class CryptoData_15min(models.Model):
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
    
class StockData_15min(models.Model):
    symbol = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    current_price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    percent_change = models.FloatField()
    volume = models.FloatField()
    
    def __str__(self):
        return f"{self.symbol} - {self.datetime}"
    
User = get_user_model()

class AccountBalance(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Account {self.user_id.username} Balance: {self.balance}"


class StockOrder(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    day_trading = models.BooleanField()
    long_term_invest = models.BooleanField()
    symbol = models.CharField(max_length=50)
    sell = models.BooleanField()
    buy = models.BooleanField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField()
    end_date = models.DateTimeField(auto_now_add=True)
    stop_loss = models.FloatField()
    take_profit = models.FloatField()

    def __str__(self):
        return f"{self.id},{self.user_id.username},{self.symbol},{self.amount}" 
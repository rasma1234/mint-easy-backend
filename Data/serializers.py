from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AccountBalance, StockOrder

User = get_user_model()

# class AccountBalanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AccountBalance
#         fields = '__all__'
class AccountBalanceSerializer(serializers.ModelSerializer):
    profit_loss = serializers.SerializerMethodField()

    class Meta:
        model = AccountBalance
        fields = ['id', 'balance', 'created_at', 'updated_at', 'user_id', 'profit_loss']

    def get_profit_loss(self, instance):
        return getattr(instance, 'stock_value', 0)
    


class StockOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOrder
        fields = '__all__'
        # fields = ['user_id', 'start_date', 'day_trading', 'long_term_invest',
        #           'symbol', 'sell', 'buy', 'open_price', 'close_price', 'quantity',
        #           'amount', 'end_date', 'stop_loss', 'take_profit']

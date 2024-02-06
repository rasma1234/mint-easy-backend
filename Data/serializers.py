from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import AccountBalance, StockOrder

User = get_user_model()

class AccountBalanceSerializer(serializers.ModelSerializer):
    profit_loss = serializers.SerializerMethodField()

    class Meta:
        model = AccountBalance
        fields = ['id', 'balance', 'created_at', 'updated_at', 'user_id', 'profit_loss', 'stock_amount']

    def get_profit_loss(self, instance):
        return getattr(instance, 'stock_value', 0)
    

class StockOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOrder
        fields = '__all__'


class ChatResponseSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    chat_response = serializers.CharField()

from rest_framework import generics, permissions
from .models import AccountBalance, StockOrder
from .serializers import AccountBalanceSerializer, StockOrderSerializer
from django.views.generic import DetailView, ListView
from rest_framework import generics, permissions
from .models import StockOrder
from .serializers import StockOrderSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import AccountBalance, StockOrder, StockData, Stockordercounter
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import StockOrder, StockData
from .serializers import StockOrderSerializer

class AccountBalanceDetailView(generics.RetrieveAPIView):
    serializer_class = AccountBalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        #print(f'User:{user}')
        stock_orders_count = StockOrder.objects.filter(user_id=user.id).count()
        stock_counter, created = Stockordercounter.objects.get_or_create(user_id=user)
        #print(f'Stockcounter: {stock_counter.counter}')
        if created:
            stock_counter.counter = 0
            stock_counter.save()
        #print(f'Stock_Orders:{stock_orders_count}')
        try:
            account_balance = AccountBalance.objects.get(user_id=user)
            stock_order = StockOrder.objects.filter(user_id=user).first()
            stock_symbol = stock_order.symbol
            stock_quantity = stock_order.quantity
            account_balance.stock_value = self.get_stock_value(stock_symbol, stock_quantity, stock_order)
            account_balance.stock_amount = stock_order.amount
            #print(account_balance.stock_amount)  # Set current_invest based on StockOrder
            account_balance.save()
        except AccountBalance.DoesNotExist:
            account_balance = AccountBalance.objects.create(user_id=user, balance=100000)
        if stock_counter.counter != stock_orders_count:
            #print(f"Number of orders has changed. Current count: {stock_counter.counter}")
            #print(f'Stock Orders: {stock_orders_count}')
            if stock_counter.counter < stock_orders_count:
                stock_order = StockOrder.objects.filter(user_id=user).first()
                stock_amount = stock_order.amount
                account_balance.balance -= stock_amount
                if account_balance.balance < 0:
                    account_balance.balance = 0
                # Calculate and set stock_value directly in retrieve method
                stock_data = StockData.objects.filter(symbol=stock_symbol).order_by('datetime').first()
                if stock_data:
                    stock_value = (stock_data.current_price - stock_order.open_price) * stock_quantity
                else:
                    stock_value = 0
                account_balance.stock_value = stock_value       
                account_balance.save()
                #print(self.previous_orders_count)
            stock_counter.counter = stock_orders_count
            stock_counter.save()
            #print(f'The last: {stock_counter.counter}')
        return account_balance
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Serialize the instance
        serializer = self.get_serializer(instance)
        # Add 'Profit_Loss' field to the serialized data
        serializer.data['profit_loss'] = instance.stock_value 
        serializer.data['stock_amount'] = instance.stock_amount
        return Response(serializer.data)

    def get_stock_value(self, symbol, quantity, stock_order):
        try:
            # Retrieve the most recent StockData based on the datetime field
            stock_data = StockData.objects.filter(symbol=symbol).order_by('datetime').first()
            #print(stock_data)
            if stock_data:
                # Implement your logic to calculate stock value based on stock data and quantity
                result = (stock_data.current_price - stock_order.open_price) * quantity
                #print("Stock Value Calculation Result:", result)
                return result  # Replace with your actual logic
            else:
                # Handle the case when no stock data is found for the given symbol
                return 0  # You may want to handle this differently based on your requirements

        except StockData.DoesNotExist:
            # Handle the case when no stock data is found for the given symbol
            return 0  # You may want to handle this differently based on your requirements



class StockOrderProfitLossView(generics.RetrieveAPIView):
    serializer_class = StockOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        stock_order = StockOrder.objects.filter(user_id=user).first()
        print(stock_order)

        if stock_order:
            most_recent_stock_data = StockData.objects.filter(symbol=stock_order.symbol, datetime__lte=stock_order.start_date).order_by('-datetime').first()
            print(most_recent_stock_data)
            
            return stock_order, most_recent_stock_data

        else:
            return None, None

    def retrieve(self, request, *args, **kwargs):
        stock_order, most_recent_stock_data = self.get_object()

        if not stock_order:
            return Response({"detail": "Stock Order not found."}, status=404)

        profit_loss = 0
        if stock_order.sell:
            # For sell orders, profit_loss = (close_price - open_price) * quantity
            profit_loss = (stock_order.close_price - most_recent_stock_data.current_price) * stock_order.quantity
        elif stock_order.buy:
            # For buy orders, profit_loss = 0 (assuming no profit or loss until the stock is sold)
            profit_loss = 0

        serializer = self.get_serializer(stock_order)
        data = serializer.data
        data['profit_loss'] = profit_loss
        return Response(data)


class StockOrderCRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StockOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        order_id = self.kwargs.get('pk')
        print(f"User: {user}, Order ID: {order_id}")

    def get_queryset(self):
        user = self.request.user
        return StockOrder.objects.filter(user_id=user)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

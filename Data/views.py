# from rest_framework import generics, permissions
# from .models import AccountBalance, StockOrder
# from .serializers import AccountBalanceSerializer, StockOrderSerializer
# from django.views.generic import DetailView, ListView
# from rest_framework import generics, permissions
# from .models import StockOrder
# from .serializers import StockOrderSerializer
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from .models import AccountBalance, StockOrder, StockData, Stockordercounter
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from .models import StockOrder, StockData
# from .serializers import StockOrderSerializer, ChatResponseSerializer
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from .models import StockOrder, Stockordercounter, AccountBalance, StockData
# from .serializers import AccountBalanceSerializer
# # import os
# # from vertexai import init
# # from vertexai.preview.generative_models import GenerativeModel, ChatSession
# # from rest_framework import generics, permissions, status
# # from django.urls import reverse
# # from rest_framework.response import Response
# from rest_framework.views import APIView
# # import requests
# # from datetime import datetime 
# # import statsmodels.api as sm
# # from datetime import datetime, timedelta
# # import pandas as pd
# from rest_framework import generics, permissions
# from .models import AccountBalance, StockOrder, StockData, Stockordercounter
# from .serializers import AccountBalanceSerializer, StockOrderSerializer, ChatResponseSerializer
# from django.views.generic import DetailView, ListView
# import os
# from vertexai import init
# from vertexai.preview.generative_models import GenerativeModel, ChatSession
# import statsmodels.api as sm
# from datetime import datetime, timedelta
# import pandas as pd
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import AccountBalance, StockOrder, StockData, Stockordercounter
from .serializers import AccountBalanceSerializer, StockOrderSerializer, ChatResponseSerializer
from django.views.generic import DetailView, ListView
import os
from vertexai import init
from vertexai.preview.generative_models import GenerativeModel, ChatSession
from django.urls import reverse
from rest_framework.views import APIView
from datetime import datetime, timedelta
import pandas as pd


class AccountBalanceDetailView(generics.RetrieveAPIView):
    serializer_class = AccountBalanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        user = self.request.user
        print(f'User:{user}')
        stock_orders_count = StockOrder.objects.filter(user_id=user.id).count()
        stock_counter, created = Stockordercounter.objects.get_or_create(user_id=user)
        print(f'Stockcounter: {stock_counter.counter}')
        if created:
            stock_counter.counter = 0
            stock_counter.save()
        print(f'Stock Counter: {stock_orders_count}')
        if stock_orders_count == 0:
            # Return data when stock_orders_count is zero
            return {
                'balance': 100000,
                'user_id': user.id,
                'profit_loss': 0,
                'stock_amount': 0,
            }
        try:
            account_balance = AccountBalance.objects.get(user_id=user)
            stock_order = StockOrder.objects.filter(user_id=user).first()
            stock_symbol = stock_order.symbol
            stock_quantity = stock_order.quantity
            account_balance.stock_value = self.get_stock_value(stock_symbol, stock_quantity, stock_order)
            account_balance.stock_amount = stock_order.amount
            account_balance.save()
        except AccountBalance.DoesNotExist:
            account_balance = AccountBalance.objects.create(user_id=user, balance=100000)
        if stock_counter.counter != stock_orders_count:
            if stock_counter.counter < stock_orders_count:
                stock_order = StockOrder.objects.filter(user_id=user).first()
                stock_amount = stock_order.amount
                account_balance.balance -= stock_amount
                if account_balance.balance < 0:
                    account_balance.balance = 0
                stock_data = StockData.objects.filter(symbol=stock_symbol).order_by('datetime').first()
                if stock_data:
                    stock_value = (stock_data.current_price - stock_order.open_price) * stock_quantity
                else:
                    stock_value = 0
                account_balance.stock_value = stock_value
                account_balance.save()
            stock_counter.counter = stock_orders_count
            stock_counter.save()
        return account_balance
    def retrieve(self, request, *args, **kwargs):
        instance_data = self.get_object()
        # Check if instance_data is a dictionary
        if isinstance(instance_data, dict):
            return Response(instance_data)
        serializer = self.get_serializer(instance_data)
        serializer.data['profit_loss'] = instance_data.stock_value
        serializer.data['stock_amount'] = instance_data.stock_amount
        return Response(serializer.data)
    def get_stock_value(self, symbol, quantity, stock_order):
        try:
            stock_data = StockData.objects.filter(symbol=symbol).order_by('datetime').first()
            if stock_data:
                result = (stock_data.current_price - stock_order.open_price) * quantity
                return result
            else:
                return 0
        except StockData.DoesNotExist:
            return 0

class StockOrderProfitLossView(generics.RetrieveAPIView):
    serializer_class = StockOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        stock_order = StockOrder.objects.filter(user_id=user).first()
        print(stock_order)

        if stock_order:
            most_recent_stock_data = StockData.objects.filter(symbol=stock_order.symbol, datetime__lte=stock_order.start_date).order_by('datetime').first()
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


class ChatResponseSender:
    def __init__(self, symbol):
        self.symbol = symbol
        # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/dci-student/Machine_learning/top-reef-411708-6d7fd588f12b.json"
        # TODO: Update and uncomment below lines
        self.project_id = "top-reef-411708"
        self.location = "us-central1"
        init(project=self.project_id, location=self.location)
        self.model = GenerativeModel("gemini-pro")
        self.chat = self.model.start_chat()

    def get_stock_price(self):
        # Get the latest record for the symbol from the database
        latest_data = StockData.objects.filter(symbol=self.symbol).latest('datetime')
        print(latest_data)
        if latest_data:
            return latest_data.current_price
        else:
            return None
        

    def get_chat_response(self):
        # Getting the current stock price and historical data
        current_stock_price = self.get_stock_price()
        #historical_data = self.get_historical_data()

        if current_stock_price is not None:
            # Updating the prompt with the current stock price and SARIMA analysis using historical data
            prompt = f"Current stock price for {self.symbol}: {current_stock_price} USD\n\n\
                Historical data for SARIMA analysis:\n"

            # Performing SARIMA analysis with historical data
            #sarima_analysis_result = self.perform_sarima_analysis(historical_data)
            #prompt += f"{sarima_analysis_result}\n\n\
            prompt += f"\n\n\
                Objectives:\n\n\
                As a financial analyst, provide a detailed recommendation for potential investors interested in {self.symbol}.\n\
                Analyze the current stock price, market capitalization, dividend yield, and price-earnings ratio (P/E ratio).\n\
                Utilize seasonal trend analysis, overbought/oversold conditions, and trend identification using moving averages.\n\
                Provide specific entry points and short- to medium-term trend forecasts.\n\
                Explain the methodology and rationale for selected indicators and their contribution to the overall evaluation.\n\
                Provide a brief overview of economic and market-related factors influencing the recommendations.\n\
                Identify potential risks such as market volatility, economic uncertainties, or industry-specific challenges.\n\
                Highlight the impact of these risks on the accuracy of forecasts and the overall investment outlook.\n\
                Formatting:\n\n\
                Current Stock Information:\n\n\
                Stock Price\n\
                Market Capitalization\n\
                Brief Explanation: Understanding stock value and company's total worth\n\
                Dividend Yield and P/E Ratio:\n\n\
                Dividend Yield\n\
                P/E Ratio\n\
                Brief Explanation: Assessing income potential and relative valuation\n\
                Seasonal Trend Analysis (SARIMA):\n\n\
                SARIMA Implementation\n\
                Brief Explanation: Modeling and understanding seasonal trends\n\
                Overbought/Oversold Conditions (RSI):\n\n\
                RSI Integration\n\
                Brief Explanation: Assessing entry or exit points\n\
                Moving Averages for Trend Identification:\n\n\
                Application of Moving Averages\n\
                Brief Explanation: Identifying potential trends\n\
                Output:\n\n\
                Summary of Financial Analysis and Stock Recommendations for {self.symbol}\n\n\
                Current Stock Price: \n\
                Market Capitalization: \n\
                Dividend Yield: \n\
                P/E Ratio: \n\
                SARIMA Trend Analysis: Strong seasonal trend with significant sales increase during the holiday season\n\
                RSI: (not overbought, not oversold)\n\
                Moving Averages Trend Analysis: Bullish trend\n\
                Recommendations:\n\n\
                Entry Price: approx. \n\
                Short- to Medium-Term Trend: Likely upward trend\n\
                Risk Assessment:\n\n\
                Market Volatility\n\
                Economic Uncertainties\n\
                Industry-Specific Challenges\n\
                Date: {datetime.now().strftime('%d.%m.%Y')}"
        else:
            # Continue without the stock price if it cannot be retrieved
            prompt = f"We apologize, but we couldn't retrieve the current stock price for {self.symbol}."

        response = self.chat.send_message(prompt)
        return response.text
   
class RetrieveChatResponseAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the symbol from POST data
        symbol = request.data.get('symbol', '')
        # Check if the symbol is provided
        if not symbol:
            return Response({"detail": "Symbol parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        # Create an instance of ChatResponseSender with the received symbol
        chat_response_sender = ChatResponseSender(symbol)
        # Get the chat response
        chat_response = chat_response_sender.get_chat_response()
        # Construct the full URL using the request object
        api_endpoint_url = request.build_absolute_uri(reverse('retrieve-chat-response'))
        # Prepare the data to send to the Django API
        data = {
            "symbol": symbol,
            "chat_response": chat_response
        }
        # Include CSRF token in headers for POST request
        csrf_token = request.COOKIES.get('csrftoken')
        headers = {
            'X-CSRFToken': csrf_token,
            'Content-Type': 'application/json',
        }
        # Send the data to the Django API with POST
        return Response(data)

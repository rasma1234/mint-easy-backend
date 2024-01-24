from django.urls import path

from .views import (
    
    AccountBalanceDetailView,
    StockOrderProfitLossView,
    StockOrderCRUDView,
    RetrieveChatResponseAPI,
    
)

urlpatterns = [
    #path('account-balances/', AccountBalanceListCreateView.as_view(), name='account-balance-list-create'),
    path('account-balances/<int:pk>/', AccountBalanceDetailView.as_view(), name='account-balance-detail'),
    path('stock-order/<int:pk>/profit-loss/', StockOrderProfitLossView.as_view(), name='stock-order-profit-loss'),
    path('api/retrieve-chat-response/', RetrieveChatResponseAPI.as_view(), name='retrieve-chat-response'),
    path('stock-orders/<int:pk>/', StockOrderCRUDView.as_view(), name='stock-order-CRUDView'),
    #path('stock-orders/<int:pk>/', StockOrderDetailView.as_view(), name='stock-order-detail'),
]
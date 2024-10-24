from django.urls import path
from .views import CustomerStatisticsView

urlpatterns = [
    path('customer-statistics/', CustomerStatisticsView.as_view(), name='customer_statistics'),
]

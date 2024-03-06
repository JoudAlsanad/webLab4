from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('<int:num>/', views.calculate_total_price, name='alculate_total_price'),
    path('tax_rate/', views.tax_rate_view, name='tax_rate'),
]

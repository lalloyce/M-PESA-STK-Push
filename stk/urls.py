from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pay/', views.pay, name='payment'),
    path('stk_push/', views.stk_push, name='stk_push'),
]

from django.urls import path
from . import views


app_name = 'payments'

urlpatterns = [
    path('verify_card/', views.verify_card, name='verify_card'),
    path('process_payment/', views.process_payment, name='process_payment'),
]

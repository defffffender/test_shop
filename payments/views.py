# payments/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .services import verify_otp, make_payment

def verify_card(request):
    if request.method == 'POST':
        card = request.POST.get('card')
        expiry = request.POST.get('expiry')
        card_type = request.POST.get('type')
        phone = request.POST.get('phone')
        response = verify_otp(card, expiry, card_type, phone)
        return JsonResponse(response)

    return render(request, 'payments/verify_card.html')

def process_payment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('id')
        amount = request.POST.get('amount')
        account = request.POST.get('account')
        service_id = request.POST.get('serviceId')
        card_id = request.POST.get('card')
        response = make_payment(payment_id, amount, account, service_id, card_id)
        return JsonResponse(response)

    return render(request, 'payments/process_payment.html')

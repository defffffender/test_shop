import requests
from requests.auth import HTTPBasicAuth

API_HOST = 'http://example.com'

AUTH = HTTPBasicAuth('sharshara', 'pkU>t48C4)8/')

def verify_otp(card, expiry, card_type, phone):
    url = f"{API_HOST}/card/api/v2/verify/OTP"
    payload = {
        "card": card,
        "expiry": expiry,
        "type": card_type,
        "phone": phone
    }
    response = requests.post(url, json=payload, auth=AUTH)
    return response.json()

def make_payment(payment_id, amount, account, service_id, card_id):
    url = f"{API_HOST}/payment/api/v1/pay"
    payload = {
        "id": payment_id,
        "amount": amount,
        "account": account,
        "serviceId": service_id,
        "card": card_id
    }
    response = requests.post(url, json=payload, auth=AUTH)
    return response.json()

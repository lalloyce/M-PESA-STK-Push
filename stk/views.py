from django.shortcuts import render
from django.http import HttpResponse
from .credentials import MpesaAccessToken, MpesaPassword
import requests

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pay(request):
    return render(request, 'pay.html')    

def stk_push(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.MpesaAccessToken
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
        headers = {
            "Authorization": "Bearer %s" % access_token
        }
        request_data = {
            "BusinessShortCode": MpesaPassword.business_short_code,    
            "Password": MpesaPassword.decoded_password,    
            "Timestamp": MpesaPassword.timestamp,
            "TransactionType": "CustomerPayBillOnline",    
            "Amount": amount,    
            "PartyA": phone,    
            "PartyB": MpesaPassword.business_short_code,        
            "PhoneNumber": phone,    
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",    
            "AccountReference": "Test",    
            "TransactionDesc": "Test"
        }
        
        response = requests.post(api_url, json=request_data, headers=headers)
        return HttpResponse('Payment initiated successfully')
    return HttpResponse('Invalid request method')
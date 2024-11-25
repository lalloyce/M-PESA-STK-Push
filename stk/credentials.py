import requests
import json
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
import base64

class MpesaCredentials:
    consumer_key = os.getenv('MPESA_CONSUMER_KEY', 'your-consumer-key')
    consumer_secret = os.getenv('MPESA_CONSUMER_SECRET', 'your-consumer-secret')
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

class MpesaAccessToken:
    r = requests.get(
        MpesaCredentials.api_url, 
        auth=HTTPBasicAuth(MpesaCredentials.consumer_key, MpesaCredentials.consumer_secret)
        )
    MpesaAccessToken=json.loads(r.text)['access_token']
        
class MpesaPassword:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    passkey = os.getenv('MPESA_PASSKEY', 'your-passkey')
    business_short_code = os.getenv('MPESA_BUSINESS_SHORT_CODE', '174379')
    OffsetValue = '0'

    data_to_encode = business_short_code + passkey + timestamp
    online_password = base64.b64encode(data_to_encode.encode())
    decoded_password = online_password.decode('utf-8')
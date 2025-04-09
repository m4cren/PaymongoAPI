from flask import Blueprint, request, jsonify
import requests
from ..db_config import PAYMONGO_API_KEY, PAYMONGO_API_URL, encode_api_key

encoded_key = encode_api_key(PAYMONGO_API_KEY)

def create_payment_link(amount, description, remarks):
    payload = {
        'data':{
            'attributes':{
                'amount': amount * 100,
                'description': description,
                'remarks': remarks,
                'currency': 'PHP',
                'redirect':{
                     'success':'http://192.168.1.33:1000/paid',
                     'failed': 'http://192.168.1.33:1000/unsuccesful'
                }
            }
        }
    }

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'authorization': f'Basic {encoded_key}'
    }

    response = requests.post(PAYMONGO_API_URL, json=payload, headers=headers)
    data = response.json()

    try:
        checkout_url = data['data']['attributes']['checkout_url']
        return {'checkout_url': checkout_url}
    except KeyError:
        return {'error': 'Payment link creation failed', 'details': data}


paymongo = Blueprint('paymongo', __name__)

@paymongo.route('/paymongo/payment', methods=['POST'])
def paymongo_payment():
     data = request.json

     price = data.get('price_to_pay')
     
     result = create_payment_link(price, 'Hello world', 'test')

     return jsonify(result)




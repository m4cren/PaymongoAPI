


from .extensions import db






from dotenv import load_dotenv
import os
import base64
load_dotenv()

PAYMONGO_API_KEY = os.getenv('PAYMONGO_API_KEY')
PAYMONGO_API_URL = 'https://api.paymongo.com/v1/links'

def encode_api_key(api_key):
    return base64.b64encode(api_key.encode()).decode()



def save_data(data):

    try:
        db.session.add(data)
        db.session.commit()

        return "success"
    except:
        db.session.rollback()
        return "failed"



def delete_data(data):

    try:
        db.session.delete(data)
        db.session.commit()

        return "success"
    except:
        db.session.rollback()
        return "failed"



def delete_all_data(data):

    try:
        for x in data:
            db.session.delete(x)
        db.session.commit()

        return "success"
    except:
        db.session.rollback()
        return "failed"

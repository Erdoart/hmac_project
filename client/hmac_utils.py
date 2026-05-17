import hmac
import hashlib

from shared.config import SECRET_KEY

def generate_hmac(message):
    
    generated_hmac = hmac.new(

        SECRET_KEY.encode(),

        message.encode(),

        hashlib.sha256

    ).hexdigest()
    
    return generated_hmac
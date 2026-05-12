import hmac
import hashlib

from shared.config import SECRET_KEY


def verify_hmac(message, received_hmac):

    generated_hmac=hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(
        generated_hmac,
        received_hmac
    )

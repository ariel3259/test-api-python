from authlib.jose import jwt
from authlib.jose.errors import BadSignatureError
from datetime import datetime
from flask import current_app

def encode_jwt(user_id, email):
    now = datetime.now()
    hour = now.hour + 1
    minute = now.minute + 30
    if minute > 60:
        minute -= 60
        hour += 1
    expire_in = datetime(now.year, now.month, now.day, hour, minute, now.second)
    header = {
        "alg": "HS512"
    }
    payload = {
        "iis": "localhost",
        "sub": user_id,
        "email": email,
        "iat": expire_in.timestamp().__ceil__()
    }
    with current_app.app_context():
        secret = current_app.config["SECRET"]
    return jwt.encode(header, payload, secret).decode("utf-8")

def decode_jwt(token):
    with current_app.app_context():
        secret = current_app.config["SECRET"]
    try:
        claims =  jwt.decode(token, secret)
        return claims
    except BadSignatureError:
        return None

    


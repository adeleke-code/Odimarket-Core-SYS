import jwt

# The JWT token you want to decode
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvdHBJRCI6IlhiYmFXNXlONVc2cGFTaHdnWEl0IiwiZW1haWwiOiJmZW1pYWRlbGVrZTYwMUBnbWFpbC5jb20iLCJpYXQiOjE2NzE5ODk3Mzl9.F3vbtQSue3coxs-7J4IIi1p6fjKcyrRsSYaSTzKYOQk'

# The secret key used to sign the JWT
secret = 'secret'

# Decode the JWT and extract the payload
payload = jwt.decode(token, secret, algorithms='HS256')

print(payload)  # {'key': 'value'}

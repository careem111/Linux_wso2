import hashlib,sys

arg_val = sys.argv[1]
password = bytes(arg_val, 'utf-8')
salt = b'Km5d5ivMy8iexuHcZrsD'

dk = hashlib.pbkdf2_hmac('sha512', password, salt, 200000)
pass_value = dk.hex()
print(pass_value)

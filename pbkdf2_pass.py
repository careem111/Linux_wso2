import hashlib,sys
import secrets

n=16
salt = secrets.token_hex(n)

arg_val = sys.argv[1]
password = bytes(arg_val, 'utf-8')

dk = hashlib.pbkdf2_hmac('sha512', password, salt.encode(), 200000)
pass_value = dk.hex()
print(pass_value)

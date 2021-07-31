import hashlib,sys
import secrets

n=16
salt = secrets.token_hex(n)

password = sys.argv[1]

hp = hashlib.sha512((password+salt).encode())
pass_value = hp.hexdigest()
print(pass_value)

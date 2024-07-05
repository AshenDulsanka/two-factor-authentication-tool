import time
import pyotp

key = pyotp.random_base32()

totp = pyotp.TOTP(key)

print(totp.now())

input_code = input("Enter 2FA Code: ")

print(totp.verify(input_code))
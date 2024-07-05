import time
import pyotp
import qrcode

key = pyotp.random_base32()

name = input("Enter your name: ")

uri = pyotp.totp.TOTP(key).provisioning_uri(name=name, issuer_name="2FA Test")

print(uri)

qrcode.make(uri).save("otp.png")
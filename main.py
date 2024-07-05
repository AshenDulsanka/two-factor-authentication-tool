import time
import pyotp
import qrcode

key = "JBSWY3DPEHPK3PXP"

name = input("Enter your name: ")

uri = pyotp.totp.TOTP(key).provisioning_uri(name=name, issuer_name="2FA Test")

print(uri)

qrcode.make(uri).save("otp.png")

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter OTP: ")))
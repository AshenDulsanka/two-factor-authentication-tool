import time
import pyotp

key = pyotp.random_base32()

print("Key: ", key)
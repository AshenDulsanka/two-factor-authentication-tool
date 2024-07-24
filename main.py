import time
import pyotp
import qrcode
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = Tk()
window.title("2FA App")
window.geometry("500x500")
window.resizable(True, True)
window.iconbitmap("knivzz.ico")

key = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(key)

def gen_qr():
    name = name_box.get()
    uri = pyotp.totp.TOTP(key).provisioning_uri(name=name, issuer_name="2FA Test")
    qr = qrcode.make(uri)
    qr.save("otp.png")
    img = Image.open("otp.png")
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img
    otp_frame.pack(pady=10)

def verify_otp():
    otp = otp_box.get()
    if totp.verify(otp):
        result_label.config(text="OTP Valid!", fg="green")
    else:
        result_label.config(text="OTP Invalid!", fg="red")

lf = LabelFrame(window, text="Enter your name or email")
lf.pack(pady=10)

name_box = Entry(lf, font=("Poppins", 24), width=25, justify=CENTER)
name_box.pack(pady=10, padx=10)

button_frame = Frame(window)
button_frame.pack(pady=20)

gen_button = Button(button_frame, text="Generate QR Code", command=gen_qr)
gen_button.pack()

img_label = Label(window)
img_label.pack(pady=20)

otp_frame = LabelFrame(window, text="Scan the QR Code and enter the OTP")
otp_box = Entry(otp_frame, font=("Poppins", 24), width=25, justify=CENTER)
otp_box.pack(pady=10, padx=10)

verify_button = Button(otp_frame, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

result_label = Label(otp_frame, font=("Poppins", 18))
result_label.pack(pady=10)

window.mainloop()
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
    qrcode.make(uri).save("otp.png")
    print(uri)
    img = PhotoImage(file="otp.png")
    img_label = Label(window, image=img)
    img_label.pack(pady=20)

    lf = LabelFrame(window, text="Scan the QR Code and enter the OTP")
    lf.pack(pady=10)

    otp_box = Entry(lf, font=("Poppins, 24"), width=25, justify=CENTER)
    otp_box.pack(pady=10, padx=10)

lf = LabelFrame(window, text="Enter your name or email")
lf.pack(pady=10)

name_box = Entry(lf, font=("Poppins, 24"), width=25, justify=CENTER)
name_box.pack(pady=10, padx=10)

name = name_box.get()

button_frame = Frame(window)
button_frame.pack(pady=20)

gen_button = Button(button_frame, text="Generate QR Code", command=gen_qr)
gen_button.grid(row=0, column=0, padx=10)

window.mainloop()
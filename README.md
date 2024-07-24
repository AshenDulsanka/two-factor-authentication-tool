# Two Factor Authentication tool

This is a simple Python application that generates a QR code for Two-Factor Authentication (2FA) using the TOTP algorithm. You can use this application to secure your accounts with an additional layer of authentication.

## Features

- Generate a QR code for TOTP-based 2FA.
- Verify OTPs generated from authenticator apps.
- User-friendly GUI built with Tkinter.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- `pyotp` library
- `qrcode` library
- `Pillow` library (for image handling)
- `tkinter` (usually included with Python installations)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/2fa-app.git
   cd 2fa-app
   ```
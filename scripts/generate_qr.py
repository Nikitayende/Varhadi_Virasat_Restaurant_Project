import qrcode
import os

# Replace with your computer's IP address
BASE_URL = "http://192.168.1.25:5000/table"

os.makedirs("static/images/table_qr", exist_ok=True)

for table in range(1, 31):
    url = f"{BASE_URL}/{table}"

    img = qrcode.make(url)

    img.save(f"static/images/table_qr/table_{table}.png")


print("QR Codes Generated Successfully!")
'''
This small script will generate a QR-Code for any text data you want. 

Requirements:
- Python qrcode library, you can install via pip: # pip install qrcode
- Pillow: # pip install Pillow
'''

# Importing required library
import qrcode
from PIL import Image

# Insert here the data you want to encode in the QR Code 
data = "https://jaolahy.com"

# Generate QR-code
# You can modify and adjust the size and frame of your QR-Code
qr = qrcode.QRCode(version = 1, box_size = 10, border=5)
qr.add_data(data)
qr.make(fit = True)

# Create an image from the generated QR-Code
# You can change the colors
image = qr.make_image(fill_color = "black", back_color = "white")

# Save the created image in the parent directory the script location
image.save("qr_code.png")
#image.open("qr_code.png") ## Somehow not VSCode on Windows is not able to open the image

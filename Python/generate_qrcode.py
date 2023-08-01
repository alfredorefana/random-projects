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
# TODO: amend to be typed as input of the scripts 
data = "https://jaolahy.com"

# Generate QR-code. You can modify and adjust the size and frame of your QR-Code
qr = qrcode.QRCode(version = 1,     # Version: This parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21×21 matrix).
                   box_size = 10,   # box_size: This parameter controls how many pixels each “box” of the QR code is.
                   border = 5)      # border: The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum in the specification).
qr.add_data(data)                   # add_data(): This method is used to add data to the QRCode object. It takes the data to be encoded as a parameter.
qr.make(fit = True)                 # make(): This method with (fit=True) ensures that the entire dimension of the QR Code is utilized, even if our input data could fit into less number of boxes.

# Create an image from the generated QR-Code. You can change the colors
# make_image(): This method is used to convert the QRCode object into an image file. It takes the fill_color and back_color optional parameters to set the foreground and background color.
image = qr.make_image(fill_color = "black",     # foreground color 
                      back_color = "white")     # background color

# Save the created image in the parent directory the script location
image.save("qr_code.png")
#image.open("qr_code.png") ## Somehow not VSCode on Windows is not able to open the image

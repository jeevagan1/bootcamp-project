import pyqrcode
import png
from pyqrcode import QRCode
s = input("url ?") 
url = pyqrcode.create(s)
url.svg("qrcode.svg", scale = 8)
url.png("qrcode.png", scale = 6)
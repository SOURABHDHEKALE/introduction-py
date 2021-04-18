

import pyqrcode
import png
from pyqrcode import QRCode
QRstring ="https://www.python.org/"
url = pyqrcode.create(QRstring)
url.png('desktop\\qr.png', scale = 8)
foursquare
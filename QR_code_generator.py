import pyqrcode
from pyqrcode import QRCode

s ="https://www.youtube.com/channel/UCgUssfwWVUePPAcVRwe23nA"

url = pyqrcode.create(s)

url.svg("myyoutube.svg", scale = 8)

import pyqrcode
import png
link = "https://www.deccanherald.com/"
qr_code = pyqrcode.create(link)
qr_code.png("news.png", scale=5)


#pip install PyQRCode
#pip install pypng
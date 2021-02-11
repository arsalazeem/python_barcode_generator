import pyqrcode
import io

url =pyqrcode
url.svg('uca.svg', scale=4)
# in-memory stream is also supported
buffer = io.BytesIO()
url.svg(buffer)
# do whatever you want with buffer.getvalue()
print(list(buffer.getvalue()))
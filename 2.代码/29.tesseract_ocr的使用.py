import pytesseract
from PIL import Image

img = Image.open('yzm2.jpg')
code = pytesseract.image_to_string(img)
print(code)

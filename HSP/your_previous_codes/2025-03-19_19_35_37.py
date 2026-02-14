from PIL import Image, ImageFilter
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image_path = 'screenshot.png'
img = Image.open(image_path)
img = img.convert('L')
img = img.filter(ImageFilter.SMOOTH)
text = pytesseract.image_to_string(img, lang='eng')
print(text)
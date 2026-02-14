from PIL import Image
import pytesseract

def extract():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = Image.open("G:\\MY_AI\\MY_AI\\temp\\cropped_area.png")
    extracted_text = pytesseract.image_to_string(image)
    with open("G:\\MY_AI\\MY_AI\\temp\\extracted_text.txt", "w") as f:
        f.writelines(extracted_text)
        print(extracted_text)
extract()
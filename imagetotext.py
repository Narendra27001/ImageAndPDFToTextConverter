import os
import pytesseract	
from PIL import Image

directory = r'./InputImage'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        img = Image.open(os.path.join(directory, filename))
        pytesseract.pytesseract.tesseract_cmd =r'./Supporting_files/Tesseract-ocr/tesseract.exe'
        result = pytesseract.image_to_string(img)
        outputfile=r"./Output/{}.txt".format(filename[:-4])
        with open(outputfile,mode ='w') as file:
            file.write(result)
    else:
        continue

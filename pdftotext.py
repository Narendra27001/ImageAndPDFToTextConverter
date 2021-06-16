from PIL import Image
import pytesseract
import sys
import pdf2image
import os

directory = r'./InputPDF'
for filename in os.listdir(directory):
	if filename.endswith(".pdf"):
		PDF_file=os.path.join(directory, filename)
		pages = pdf2image.convert_from_path(PDF_file,500,poppler_path=r'./Supporting_files/poppler-0.68.0/bin')
		image_counter = 1
		for page in pages:
			imagename = "./Buffer/page_"+filename[:-4]+str(image_counter)+".jpg"
			page.save(imagename, 'JPEG')
			image_counter += 1
		filelimit = image_counter-1
		outfile = r"./Output/{}.txt".format(filename[:-4])
		f = open(outfile, "a")
		pytesseract.pytesseract.tesseract_cmd =r'./Supporting_files/Tesseract-ocr/tesseract.exe'
		for i in range(1, filelimit + 1):
			fileimage = "./Buffer/page_"+filename[:-4]+str(i)+".jpg"
			text = str(pytesseract.image_to_string(Image.open(fileimage)))
			text = text.replace('-\n', '')
			f.write(text)
		f.close()
	else:
		continue
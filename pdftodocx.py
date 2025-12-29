from pdf2docx import Converter

pdf_file = "C:\\Users\\Samarth\\Downloads\\Latex1 (1).pdf"  # Replace with your PDF file
docx_file = "C:\\Users\\Samarth\\Downloads\\Latex1 (1).docx"  # Output DOCX file

cv = Converter(pdf_file)
cv.convert(docx_file)  # Convert the entire PDF
cv.close()
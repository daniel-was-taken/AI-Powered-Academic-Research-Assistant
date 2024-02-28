# pip install pdfminer.six
# pip install 'pdfminer.six[image]'

from pdfminer.high_level import extract_text
text = extract_text('BEtest.pdf')
# print(repr(text))
with open("text/pdfextractor.txt", "w", encoding = "utf-8") as text_file:
    text_file.write(text)



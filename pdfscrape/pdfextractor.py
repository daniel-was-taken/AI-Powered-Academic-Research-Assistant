from pdfminer.high_level import extract_text
text = extract_text('toscrape.pdf')
# print(repr(text))
print(text)


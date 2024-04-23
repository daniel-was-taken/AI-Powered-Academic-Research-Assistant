from pdfminer.high_level import extract_text
import re

text = extract_text("toscrape.pdf")
# print(text)

with open("imagescrape\imaget.txt", "w", encoding="utf-8") as text_file:
    text_file.write(text)

with open("imagescrape\imaget.txt", "r", encoding="utf-8") as text_file:
  pdfText = text_file.read()

# Split text into blocks 
blocks = pdfText.split("\n\n")

# Remove all new lines within blocks to remove arbitary line breaks
blocks = map(lambda x : x.replace("\n", ""), blocks)

# Identifying Figure Captions
captions = []
for block in blocks:
    if re.search('^fig', block, re.IGNORECASE):
        captions.append(block)

with open("imagescrape\captions.txt", "w", encoding="utf-8") as text_file:
    for caption in captions:
        text_file.write(caption + "\n")
        
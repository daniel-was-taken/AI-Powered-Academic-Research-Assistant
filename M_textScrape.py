from spire.pdf.common import *
from spire.pdf import *

# Create a PdfDocument object
doc = PdfDocument()
# Load a PDF document
doc.LoadFromFile("toscrape.pdf")

# Create an empty list to store extracted text
list = []

# Loop through the pages in the document
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    # Extract text from each page and keep white spaces
    text = page.ExtractText(True)
    # Append the extracted text to the list
    list.append(text)

# Write the extracted text into a text file
with open("ExtractTextFromDocument.txt", "w", encoding = "utf-8") as text_file:
    for text in list:
        text_file.write(text + "\n")

# Close the PdfDocument object
doc.Close()
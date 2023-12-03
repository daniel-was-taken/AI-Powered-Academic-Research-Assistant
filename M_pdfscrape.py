import fitz 
doc = fitz.open('BEtest.pdf') 
text = "" 
for page in doc: 
    text += page.get_text() 

output_file = 'text/textscrape2.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)

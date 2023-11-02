from pdfminer.high_level import extract_text

text = extract_text("toscrape.pdf")
output_file = 'text/textcontent.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)
        

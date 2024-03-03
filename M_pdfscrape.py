import fitz 
def pdfscrape(name):
    # doc = fitz.open('BEtest.pdf')
    doc = fitz.open(name)
    text = "" 
    for page in doc: 
        text += page.get_text() 

    output_file = 'text/' + name + '.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

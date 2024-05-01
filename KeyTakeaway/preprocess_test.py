f = open('text/NewPdf0.txt', 'r', encoding='utf-8')

cleaned_data = ""
for sentence in f.readlines():
    if len(sentence.split()) > 4:
        cleaned_data += sentence

with open("KeyTakeaway/cleanTest.txt", 'w', encoding='utf-8') as f:
    f.write(cleaned_data)
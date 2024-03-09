import pandas as pd
import re
import numpy as np  
import nltk
from spacy.lang.en.stop_words import STOP_WORDS

def clean_data(filename, output_filename):
    try:
        with open(filename, 'r', encoding='latin-1') as f:
            data = f.read()
        newText = data.lower()
        newText = re.sub('[^\w\s\d\.,"]','',newText)
        newText = ' '.join(newText.split())
        tokens = [w for w in newText.split() if not w in STOP_WORDS]
        long_words=[]
        for i in tokens:
            if len(i)>=3:
                long_words.append(i)   
                
        cleaned_data = ' '.join([str(elem) for elem in long_words]).strip()
        # cleaned_data = re.sub(r'\s{2,}', '\n', data) #Extra spaces
        cleaned_data = re.sub(r'[^a-zA-Z0-9\s.,"]','', cleaned_data)  #Anything except alpha numeric except whitespace

        with open(output_filename, 'w') as f:
            f.write(cleaned_data)

        print(f"Data cleaned and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# clean_data('text/textcontent.txt', 'cleaned2.txt')


# def clean_body(text):
#     newText = text.lower()
#     newText = re.sub('[^\w\s\d\.]','',newText)
#     newText = ' '.join(newText.split())
#     tokens = [w for w in newText.split() if not w in STOP_WORDS]
#     long_words=[]
#     for i in tokens:
#         if len(i)>=3:
#             long_words.append(i)   
#     return (" ".join(long_words)).strip()

# cleaned_body = []
# for t in data['body']:
#     cleaned_body.append(clean_body(t))

import pandas as pd
import re

def clean_data(filename, output_filename):

    try:
        with open(filename, 'r', encoding='latin-1') as f:
            data = f.read()
        # with open(filename, 'r') as f:
        #     data = f.read()

        cleaned_data = re.sub(r'\s{2,}', '\n', data) #Extra spaces
        cleaned_data = re.sub(r'[^a-zA-Z0-9\s]','', cleaned_data)  #Anything except alpha numeric except whitespace

        with open(output_filename, 'w') as f:
            f.write(cleaned_data)

        print(f"Data cleaned and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

clean_data('text/textscrape2.txt', 'cleaned.txt')

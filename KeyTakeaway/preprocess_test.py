import re

def preprocess(filename):
    f = open(filename, 'r', encoding='utf-8')

    cleaned_data = ""
    for sentence in f.readlines():
        if len(sentence.split()) > 4:
            cleaned_data += sentence
            cleaned_data = re.sub(r'\bhttp[s]?://\S+\b', '', cleaned_data)  # Remove URLs
            cleaned_data = re.sub(r'\s+', ' ', cleaned_data)  # Replace multiple spaces with a single space
            cleaned_data = re.sub(r'\s([.,!?])', r'\1', cleaned_data)  # Remove spaces before punctuation
            # Remove multiple dots and inconsistencies
            cleaned_data = re.sub(r'\.{2,}', '', cleaned_data)  # Remove multiple dots
            # cleaned_data = re.sub(r"[^\w\s]", "", cleaned_data)

    with open("KeyTakeaway/cleanTest.txt", 'w', encoding='utf-8') as f:
        f.write(cleaned_data)
import re  # Regular expressions library

# Example function to read text from a PDF (replace with your actual scraping method)
def read_pdf_text(filepath):
  # Implement your PDF reading logic here
  # This example returns a placeholder string
  return "This is some text extracted from a PDF."

def clean_text(text):
  """
  This function pre-processes and tokenizes text data.

  Args:
      text (str): Text data to be cleaned.

  Returns:
      list: List of cleaned tokens.
  """
  # Remove special characters and multiple whitespaces
  text = re.sub(r"[^\w\s]", "", text)
  text = re.sub(r"\s+", " ", text)
  # Convert to lowercase
  text = text.lower()
  # Tokenize the text
  tokens = text.split()
  return tokens

# Example usage
# pdf_text = read_pdf_text("your_pdf_file.pdf")


# Print the cleaned tokens
# print(cleaned_tokens)

with open("text/textcontent.txt", "r", encoding="utf-8") as f:
        input_text = f.read()


input_text_string = '\n'.join(input_text)
cleaned_tokens = clean_text(input_text_string)
print(cleaned_tokens)
cleaned_tokens_string = ''.join(cleaned_tokens)

with open("text/text_preprocess.txt", "w", encoding = "utf-8") as text_file:
    text_file.write(cleaned_tokens_string)

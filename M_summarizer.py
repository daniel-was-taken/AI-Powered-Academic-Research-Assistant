# Read the file and store the input in a variable
with open("text/textscrape2.txt", "r", encoding="utf-8") as f:
    input_text = f.read()

from transformers import LongT5ForConditionalGeneration, AutoTokenizer

# Load pre-trained T5 model and tokenizer
model_name = "google/long-t5-tglobal-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = LongT5ForConditionalGeneration.from_pretrained(model_name)

# Tokenize and generate summary
input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=16384 , truncation=True)
summary_ids = model.generate(input_ids, max_length=16384)

# Decode the summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
# print("Original text:", input_text)
# print("Summary:", summary)

output_file = 'text/summary.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(summary)


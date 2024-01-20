# Read the file and store the input in a variable
with open("text/textscrape2.txt", "r", encoding="utf-8") as f:
    input_text = f.read()

from transformers import LongT5ForConditionalGeneration, AutoTokenizer
from transformers import pipeline
import torch
import datetime

start = datetime.datetime.now()
print(start)

# pipe = pipeline("summarization", model="Falconsai/text_summarization")
# pipe = pipeline("summarization", model="facebook/bart-large-cnn")
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
# summarizer = pipeline(
#     "summarization",
#     "pszemraj/long-t5-tglobal-base-16384-book-summary",
#     device=0 if torch.cuda.is_available() else -1,
# )
# long_text = "Here is a lot of text I don't want to read. Replace me"

result = pipe(input_text, min_length=800, max_length = 1024 )
print(result[0]["summary_text"])

end = datetime.datetime.now()
print(end)
# # Load pre-trained T5 model and tokenizer
# model_name = "google/long-t5-tglobal-base"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = LongT5ForConditionalGeneration.from_pretrained(model_name)

# # Tokenize and generate summary
# input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=16384 , truncation=True)
# summary_ids = model.generate(input_ids, max_length=16384)

# # Decode the summary
# summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
# # print("Original text:", input_text)
# # print("Summary:", summary)

output_file = 'text/summary.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(result[0]["summary_text"])


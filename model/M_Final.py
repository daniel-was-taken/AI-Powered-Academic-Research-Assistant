from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
import torch
# from langchain.llms import HuggingFacePipeline
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
import datetime

start = datetime.datetime.now()
print(start)

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# model_id = "mistralai/Mistral-7B-Instruct-v0.1"
# model_id = "mistralai/Mistral-7B-Instruct-v0.1"
# model_id= "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"
# model = AutoModel.from_pretrained(path,local_files_only=True,device_map='auto',cache_dir = 'D:/BEProject/.cache/huggingface/hub/')
# model = AutoModelForCausalLM.from_pretrained(model_id,device_map='auto',cache_dir = 'D:/BEProject/.cache/huggingface/hub/')
# tokenizer = AutoTokenizer.from_pretrained(model_id,)

# Test prompt 1 
# vegeterian_recipe_prompt = """### Instruction: Act as a gourmet chef. 
# I have a friend coming over who is a vegetarian.
# I want to impress my friend with a special vegetarian dish. 
# What do you recommend?

# Give me two options, along with the whole recipe for each.

#  ### Answer:
#  """

# encoded_instruction = tokenizer(vegeterian_recipe_prompt,  return_tensors="pt", add_special_tokens=True)

# model_inputs = encoded_instruction.to(device)

# generated_ids = model.generate(**model_inputs, max_new_tokens=1000, do_sample=True, pad_token_id=tokenizer.eos_token_id)
# decoded = tokenizer.batch_decode(generated_ids)
# print(decoded[0])

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("daniel-was-taken/long-t5-scisumm-accelerate-v2")
model = AutoModelForSeq2SeqLM.from_pretrained("daniel-was-taken/long-t5-scisumm-accelerate-v2")

with open("text/NewPdf0.txt", "r", encoding="utf-8") as f:
    text_to_summarize = f.read()
    
text = "Provide a brief summary of the following: " + text_to_summarize


input_ids = tokenizer.encode(text, return_tensors="pt")
generated_sequence = model.generate(input_ids=input_ids)
output_text = tokenizer.decode(generated_sequence.squeeze(), skip_special_tokens=True)
print(output_text)


end = datetime.datetime.now()
print(end)

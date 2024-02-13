from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_name_or_path = "TheBloke/Mistral-7B-Instruct-v0.2-AWQ"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    low_cpu_mem_usage=True,
    device_map="cuda:0"
)

# Using the text streamer to stream output one token at a time
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

prompt = "Tell me about AI"
prompt_template=f'''<s>[INST] {prompt} [/INST]
'''

# Convert prompt to tokens
tokens = tokenizer(
    prompt_template,
    return_tensors='pt'
).input_ids.cuda()

generation_params = {
    "do_sample": True,
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_new_tokens": 512,
    "repetition_penalty": 1.1
}

# Generate streamed output, visible one token at a time
generation_output = model.generate(
    tokens,
    streamer=streamer,
    **generation_params
)

# Generation without a streamer, which will include the prompt in the output
generation_output = model.generate(
    tokens,
    **generation_params
)

# Get the tokens from the output, decode them, print them
token_output = generation_output[0]
text_output = tokenizer.decode(token_output)
print("model.generate output: ", text_output)




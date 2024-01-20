
from transformers import pipeline
# from langchain.llms import Mistral7B
from langchain_community.llms import HuggingFacePipeline
# from langchain.agents import TextGenerationAgent
from langchain.chains import LLMChain
# from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
import datetime
import torch
from transformers import BitsAndBytesConfig
# from langchain import HuggingFacePipeline
# from langchain import PromptTemplate, LLMChain
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

start = datetime.datetime.now()
print(start)

device = "cuda"

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

model_id = "mistralai/Mistral-7B-Instruct-v0.1"



model_4bit = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", quantization_config = quantization_config)
# , quantization_config=quantization_config
# model_4bit = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

# pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
tpipeline = pipeline(
        "text-generation",
        model=model_4bit,
        tokenizer=tokenizer, 
        use_cache=True,
        device_map="auto",
        max_length=500,
        do_sample=True,
        top_k=5,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
)

llm = HuggingFacePipeline(pipeline=tpipeline)
# Load model with 4-bit quantization for memory optimization
# 
# tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
# llm = Mistral7B(model_name, low_cpu_mem_usage=True)  # Load efficiently

# pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
# agent = TextGenerationAgent(llm=llm)


template = PromptTemplate(
    input_variables=["doc"],
    template="Based on this document: {doc}\nPlease identify the main points and summarize them into a concise paragraph."
)


summarize_chain = LLMChain(
    llm=llm,
    template=template
)


def summarize_text(text):
    """Summarizes a given text using Mistral-7B."""
    
    input_dict = {"doc": text}
    output = summarize_chain.run(input_dict)
    return output["output"]



with open("text/textscrape2.txt", "r", encoding="utf-8") as f:
    text_to_summarize = f.read()
print(text_to_summarize)
# text_to_summarize = """Your long text to summarize here."""
summary = summarize_text(text_to_summarize)
print(summary)

end = datetime.datetime.now()
print(end)
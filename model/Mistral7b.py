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
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# from ctransformers import AutoModelForCausalLM, AutoConfig
# from langchain_community.llms import CTransformers

start = datetime.datetime.now()
print(start)


# model_id = "mistralai/Mistral-7B-Instruct-v0.1"
cache_dir = "D:/BEProject/.cache/huggingface/hub/"
config = {'max_new_tokens': 1024, 'repetition_penalty': 1.1, 'context_length': 4096}

# config = AutoConfig.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF",)
# config.max_position_embedding = 8192

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q5_K_M.gguf", model_type="mistral", gpu_layers=3, config=config)



# context_length=4096, max_new_tokens=4096


with open("text/textscrape2.txt", "r", encoding="utf-8") as f:
    text_to_summarize = f.read()
    
text_to_summarize = "Provide a brief summary of the following:" + text_to_summarize
# print(text_to_summarize)

# text_to_summarize = "Provide a brief summary of the following: In January 2024, two forest fires prompted the National Service for Disaster Prevention and Response (SENAPRED) to issue a red alert. One occurred on 20 January in Lonquimay, Araucanía Region, and another on 26 January in Puerto Montt, Los Lagos Region.[13] On 22 January, a fire, named 'Antiquereo 2', broke out on the boundary of Portezuelo and Trehuaco in the Ñuble Region.[14] It was contained by 24 January after consuming 35 hectares (86 acres).[15] SENAPRED responded by declaring a yellow alert in Portezuelo, marking the first alert of the year in the region.[16]. By the end of January 2024, a fire originating in Florida, Biobío Region, spread to Quillón in the Ñuble Region.[17] The 'Casablanca' fire,[18] covering 69.5 hectares (172 acres) in the Peñablanca sector,[19] was extinguished through collaborative efforts between the Quillón and Florida fire departments.[20] In the last week of January 2024, a heatwave hit central Chile, with temperatures 10 to 15 °C (18 to 27 °F) above the weekly average. Anticipating an increased wildfire risk, the Meteorological Directorate of Chile issued a heat alert on 28 January, projecting temperatures of 36 to 38 °C (97 to 100 °F) in valleys and foothills of the central zone and 30 °C (86 °F) on the coast of Valparaíso, O'Higgins, and Maule regions."


print(llm(text_to_summarize))

# # text_to_summarize = """Your long text to summarize here."""
# summary = summarize_text(text_to_summarize)
# print(summary)

end = datetime.datetime.now()
print(end)


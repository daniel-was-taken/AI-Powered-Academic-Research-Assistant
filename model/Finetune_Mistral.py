from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp

# with open("text/textscrape2.txt", "r", encoding="utf-8") as f:
#     text_to_summarize = f.read()


# question = text_to_summarize
def test():
    template = """Question: {question}

    Answer: Summarize the text but maintain integrity. """

    # Answer: Let's work this out in a step by step way to be sure we have the right answer.

    prompt = PromptTemplate.from_template(template)

    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    n_gpu_layers = (
        -1
    )  # The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
    n_batch = (
        1024  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    )

    # Make sure the model path is correct for your system!

    llm = LlamaCpp(
        model_path="D:/BEProject/.cache/huggingface/hub/mistral-7b-instruct-v0.1.Q5_K_M.gguf",
        n_gpu_layers=n_gpu_layers,
        n_batch=n_batch,
        callback_manager=callback_manager,
        verbose=True,  # Verbose is required to pass to the callback manager
    )
    llm.client.verbose = False

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    # question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
    # question = "Which football team won the FIFA world cup in 2022?"
    
    
    with open("text/textscrape2.txt", "r", encoding="utf-8") as f:
        text_to_summarize = f.read()

    # llm_chain.run(question)

    # Split text into chunks based on sentence boundaries


    max_chunk_length = 1024 # 512  # Adjust this based on your desired chunk size
    sentences = text_to_summarize.split(".")
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 < max_chunk_length:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + "."

    if current_chunk:
        chunks.append(current_chunk)

    # Summarize each chunk individually
    summaries = []
    for chunk in chunks:
        question = chunk
        summary = llm_chain.run(question)
        summaries.append(summary)

    # Combine individual summaries (optional)
    combined_summary = "\n".join(summaries)  # Simple concatenation
    # Replace with more sophisticated logic for context-aware merging if needed

    print(combined_summary)


test()

from langchain.text_splitter import CharacterTextSplitter

def get_text_chunks(text:str) ->list:
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=7500, chunk_overlap=300, length_function=len
    )
    chunks = text_splitter.split_text(text)
    # print(chunks)
    return chunks

with open("text/textcontent.txt", "r", encoding="utf-8") as f:
    text_to_summarize = f.read()



chunks = get_text_chunks(text_to_summarize)

with open("test_preprocess.txt", "w", encoding = "utf-8") as text_file:
    for x in chunks:
        text_file.write(x)
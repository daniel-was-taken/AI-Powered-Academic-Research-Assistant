# Read the file and store the input in a variable
# import datetime
# start = datetime.datetime.now()
# print(start)

def get_summary(text):
    # with open("text/textcontent.txt", "r", encoding="utf-8") as f:
    #     input_text = f.read()
    # with open(text, "r", encoding="utf-8") as f:
    #     input_text = f.read()

    from textsum.summarize import Summarizer

    # summarizer = Summarizer('pszemraj/long-t5-tglobal-base-sci-simplify')
    # token_batch_length=4096,
    summarizer = Summarizer('daniel-was-taken/long-t5-tglobal-base-sci-simplify-finetuned-scisumm')
    # summary =  summarizer("text/textscrape2.txt")



    summary = summarizer.summarize_string(input_text)
    # new_summary = [ summary for x in range(4)]
    # return new_summary
    


    output_file = 'text/finetuned-summary.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summary)

    return summary
# start = datetime.datetime.now()
# print(start)


with open("text/textcontent.txt", "r", encoding="utf-8") as f:
    input_text = f.read()
get_summary(input_text)

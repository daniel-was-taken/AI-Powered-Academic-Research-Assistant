# Read the file and store the input in a variable
# import datetime
# start = datetime.datetime.now()
# print(start)

def get_summary():
    with open("text/textcontent.txt", "r", encoding="utf-8") as f:
        input_text = f.read()

    from textsum.summarize import Summarizer

    summarizer = Summarizer('pszemraj/long-t5-tglobal-base-sci-simplify')

    
    summary = summarizer.summarize_string(input_text)
    # new_summary = [ summary for x in range(4)]
    # return new_summary
    return summary

    # output_file = 'text/summary.txt'
    # with open(output_file, 'w', encoding='utf-8') as file:
    #     file.write(summary)
    
# start = datetime.datetime.now()
# print(start)


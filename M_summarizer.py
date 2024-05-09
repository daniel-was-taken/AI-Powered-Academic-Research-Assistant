from textsum.summarize import Summarizer

def get_summary(text):
    
    with open(text, "r", encoding="utf-8") as f:
        input_text = f.read()

    token_batch_length = 4096
    max_length_ratio = 0.4

    summarizer = Summarizer(
        "daniel-was-taken/long-t5-scisumm-accelerate-v2",
        use_cuda=True,
        max_length_ratio=max_length_ratio,
        token_batch_length=token_batch_length,
    )
    
    summary = summarizer.summarize_string(
        input_text,
    )    

    output_file = "text/finetuned-summary.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summary)

    return summary

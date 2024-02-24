from flask import Flask, request, redirect, render_template
from app import app
# from M_LLMSummarizer import summarize_text
# from model.Finetune_Mistral import test


@app.route("/summarise", methods=("GET","POST"))
def summarise():
    if request.method == "POST":
        input = request.form["input"]
    if not input:
        return redirect("/")    
    # summary = summarize_text(input)

    return redirect("/summary")

from flask import Flask, request, redirect, render_template
from app import app
from M_LLMSummarizer import summarize_text

@app.route("/summarise", methods=("GET","POST"))
def summarise():
    if request.method == 'POST':
        input = request.form['input']
    if not input:
        return redirect("index.html")    
    summary = summarize_text(input)
    return render_template("index.html", summary=summary)

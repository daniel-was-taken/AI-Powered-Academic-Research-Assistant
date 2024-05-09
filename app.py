from flask import Flask, render_template, request
import pandas as pd
from M_Summarizer import get_summary
from datetime import datetime
from webscrape import arxivscrape, downloadpdf 
from M_PdfScrape import pdfscrape
from M_ImageCapScrape import extract_images_and_captions
from M_LexRankSummarizer import lexrank
from M_PreProcess import preprocess_sum

import os

app = Flask(__name__)
UPLOAD_FOLDER = 'OnlyPDFs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
titles = []
keytakeaways = []

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/summary", methods=['GET', 'POST'])
def summary():
    global titles
    global keytakeaways
    if request.method == "POST":
        topic = request.form["input"]
        arxivscrape.scrape(topic)
        df = pd.read_csv("Scrape.csv")
        titles = []
        for i in range(3):
            titles.append(df.iloc[i,0])
        csv_file = "OnlyURL.csv"
        base_filename = "NewPdf"
        target_folder = "OnlyPDFs"
        downloadpdf.download_all_pdfs(csv_file, base_filename, target_folder)
        keytakeaways = []

        for i in range(3):
            pdfscrape(f'{base_filename}{i}')
            
            keytakeaways.append(lexrank(f'text/{base_filename}{i}.txt'))

        current_dateTime = datetime.now()
        inputs = []
        for i in range(3):
            print(current_dateTime)
            preprocess_sum(f'text/{base_filename}{i}.txt')
            newInput = get_summary(f'KeyTakeaway/clean_sum.txt')
            inputs.append(newInput)
            current_dateTime = datetime.now()
            print(current_dateTime)
    return render_template("summary.html", titles=titles, inputs=inputs)

@app.route("/keytakeaway")
def keytakeaway():
    global titles
    global keytakeaways
    return render_template("keytakeaway.html", titles=titles, keytakeaways=keytakeaways)

@app.route("/images")
def images():
    global titles
    base_filename = "NewPdf"
    target_folder = "OnlyPDFs/"
    pdf_location = target_folder + base_filename
    
    images_caption = []
    if len(titles) == 1:
        images_caption.append(extract_images_and_captions(f'{target_folder + titles[0]}.pdf'))
    else:
        for i in range(len(titles)):
            images_caption.append(extract_images_and_captions(f'{pdf_location}{i}.pdf'))

    return render_template("images.html", images_caption = images_caption, data_length = len(images_caption), titles= titles)

@app.route("/upload", methods=("GET","POST"))
def upload():
    if request.method == "POST":
        pdf = request.files.get("pdf")
        base_filename = pdf.filename[:-4]
        pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename))
        pdfscrape(base_filename)
        textFile = 'text/' + base_filename + '.txt'
        keytakeaways.clear()
        keytakeaways.append(lexrank(textFile))
      
        current_dateTime = datetime.now()

        print(current_dateTime)
        preprocess_sum(textFile)
        inp = get_summary(f'KeyTakeaway/clean_sum.txt')
        titles.clear()
        titles.append(base_filename)
        inputs = []
        inputs.append(inp)
        current_dateTime = datetime.now()

        print(current_dateTime)

    return render_template("summary.html", titles=titles, inputs=inputs)

if __name__ == '__main__':
    app.run(debug=True)

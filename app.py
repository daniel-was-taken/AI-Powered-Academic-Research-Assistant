from flask import Flask, render_template, request

from M_summarizer import get_summary
from datetime import datetime
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/summary", methods=['GET','POST'])
def summary():
    if request.method == "POST":
    #    input = request.form["input"]
       current_dateTime = datetime.now()

       print(current_dateTime)
       input = get_summary()
       current_dateTime = datetime.now()

       print(current_dateTime)

    if not input:
        input="HELLO WORLD"
    return render_template("summary.html", summary = input)


if __name__ == '__main__':  
   app.run(debug=True)
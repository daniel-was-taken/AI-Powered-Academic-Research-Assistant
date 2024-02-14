from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/summary", methods=['GET','POST'])
def summary():
    if request.method == "POST":
       input = request.form["input"]
    if not input:
        input="HELLO WORLD"
    return render_template("summary.html", summary = input)


if __name__ == '__main__':  
   app.run(debug=True)
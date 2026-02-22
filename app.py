from services.reader import parcing
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uploads", methods=["POST"])
def upload():
    file = request.files["file"]
    

if __name__ == "__main__":
    # app.run(debug=True)
    result = parcing("./test.xlsx")
    print(result)
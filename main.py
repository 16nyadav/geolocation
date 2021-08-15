from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/distance", methods=["POST","GET"])
def compute_address():
    if request.method == "POST":
        import pdb;pdb.set_trace()
    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
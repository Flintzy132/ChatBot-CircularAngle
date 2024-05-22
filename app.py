import os
import webbrowser
from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/nudge")
def nudge():
    text = request.get_json().get("message")
    message = {"answer": "Try typing 'How many leaves do i have left?' or 'What is the HR policy for Leaves?'"}
    return jsonify(message)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    if response == "Downloading":
        url = "http://127.0.0.1:8000/download_pdf"
        return webbrowser.open(url), jsonify(message)
    else:
        return jsonify(message)


if __name__ == "__main__":
    os.system("replace_data.py")
    app.run(debug=True)

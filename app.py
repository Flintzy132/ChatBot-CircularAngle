import os
import webbrowser
from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.route('/save_url', methods=['POST'])
def save_url():
    data = request.json
    url = data.get('url')
    print(f'The current URL is: {url}')
    return '', 204


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/nudge")
def nudge():
    message = {"answer": "Try asking for any information' or typing 'What is the HR policy for Leaves?'"}
    return jsonify(message)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    if response == "Downloading":
        url = "http://127.0.0.1:8000/download_pdf"
        return webbrowser.open(url), jsonify(message)
    if response.split()[0] == "Visit":
        url = response[response.index(" ") + 2:]
        message = {"answer": "Downloading Requested File"}
        return jsonify(message), webbrowser.open(url)
    else:
        return jsonify(message)


if __name__ == "__main__":
    os.system("replace_data.py")
    os.system("api.py")
    app.run(debug=True)

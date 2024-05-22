from flask import Flask, send_file

app = Flask(__name__)


@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    return send_file('sample_input.pdf', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

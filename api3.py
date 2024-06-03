from flask import Flask, request
from requests.models import PreparedRequest

app = Flask(__name__)


@app.route('/payslip')
def my_route():
  page = request.args.get('page', default = 1, type = int)
  filter = request.args.get('filter', default = '*', type = str)


url = 'http://example.com/search?q=question'
params = {'lang': 'en', 'tag': 'python'}
req = PreparedRequest()
req.prepare_url(url, params)
print(req.url)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/get-user/")
def get_user():
    user_data = [{"Name": "John"},
                 {"Pan Card": "EFGH5678"},
                 {"Birthday": "1st Jan 2021"},
                 {"Leave Balance": [{
                     "Earned Leave": "2"
                 }, {
                     "Casual Leave": "3"
                 }]},
                 {"HR Policy": [{
                     "Holiday": "Regular attendance is mandatory for the effective operation of the Company."
                 }, {
                     "Leaves": "You may request your supervisor for leaves but only under certain circumstances will it be accepted."
                 }]},
                 {"Supervisor": [{
                     "Name": "Mr.X"
                 }, {
                     "Contact": "XX-XXXXXXXY"
                 }]}
                 ]

    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True, port=8080)

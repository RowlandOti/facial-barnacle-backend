from flask import Flask, request

from model.facial_identifier import identify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/status', methods=['GET'])
def status():
    result = dict()
    if request.method == 'GET':
        result["success"] = "Everything seems okay"

    return result


@app.route('/api/login', methods=['POST'])
def facial_login():
    request_data = request.get_json()
    result = dict()

    name = identify(request_data['photoDownloadUrl'])

    result["email"] = request_data['email']
    result["success"] = True

    if name == "unknown":
        result["success"] = False
        return dict(message=result), 401

    return dict(message=result)


if __name__ == '__main__':
    app.run()

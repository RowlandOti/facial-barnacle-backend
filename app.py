from flask import Flask, request
from flask_cors import CORS

from model.facial_identifier import identify
from flask_seasurf import SeaSurf
from flask_talisman import Talisman

from raspi.raspi_controller import should_drive_wheels

app = Flask(__name__)
app.secret_key = "!5}2|f137<^-gTs8'nEmN]6S3eRg1u"
app.config['CSRF_CHECK_REFERER'] = False
csrf = SeaSurf(app)
CORS(app, supports_credentials=True)
talisman = Talisman(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/status', methods=['GET'])
def status():
    result = dict()
    if request.method == 'GET':
        result["success"] = "Everything seems okay"

    return result

@csrf.exempt
@app.route('/api/login', methods=['POST'])
def facial_login():
    request_data = request.get_json()
    result = dict()

    name = identify(request_data['photoDownloadUrl'])

    result["email"] = request_data['email']
    result["success"] = True

    if name == "unknown":
        result["success"] = False
        should_drive_wheels(False)
        return dict(message=result), 401

    should_drive_wheels(True)
    return dict(message=result)


if __name__ == '__main__':
    app.run()

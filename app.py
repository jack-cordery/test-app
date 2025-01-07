from flask import Flask

app = Flask(__name__)


@app.route('/version', methods=['GET'])
def about():
    message = "version 1"

    return {'message': message}, 200


@app.route('/healthz', methods=['GET'])
def about():
    message = "healthy"

    return {'message': message}, 200
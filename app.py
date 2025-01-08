from flask import Flask

app = Flask(__name__)


@app.route('/version', methods=['GET'])
def aboutAnd():
    message = "version dev"

    return {'message': message}, 200


@app.route('/healthz', methods=['GET'])
def about():
    message = "healthy"

    return {'message': message}, 200
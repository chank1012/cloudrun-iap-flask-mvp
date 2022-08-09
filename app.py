from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/headers')
def get_headers():
    return jsonify({k:v for k, v in request.headers.items()})


if __name__ == '__main__':
    app.run()


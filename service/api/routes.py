from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="OK")


def start_api():
    app.run(debug=True, use_reloader=False, port=5000)

if __name__ == '__main__':
    start_api()
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "user service is running "}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
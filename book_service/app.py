from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "book service is running"}),200

@app.route('/books',methods=['GET'])
def get_books():
    books = [
        {"id": 1, "title": "Atomic habits"},
        {"id": 2, "title": "The Hobbit"},
        {"id": 3, "title": "Fountainhead"}
    ]
    return jsonify(books), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
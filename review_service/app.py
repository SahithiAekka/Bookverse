from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "review service is running"}), 200

@app.route('/review')
def get_reviews():
    reviews = [
        {"id": 1, "book_id": 1, "review": "Amazing insights!"},
        {"id": 2, "book_id": 2, "review": "Very intresting love it!"},
        {"id": 3, "book_id": 3, "review": "I like this book"}
    ]
            
    return jsonify(reviews),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
    
    

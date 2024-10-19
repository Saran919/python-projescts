from flask import Flask, jsonify, request

app = Flask(__name__)
books = [{'id': 1, 'title': 'Python Essentials', 'author': 'Jane Doe'},{'id': 2, 'title': 'Sidhupython', 'author': 'Murali krishna'}]
abc = "Testing python"
@app.route('/sidhu', methods=['GET'])
def get_books():
    return jsonify({'books': books}), 200


@app.route('/get-user', methods=['GET'])
def get_user():
    return jsonify({'firstName': 'Siddu', 'lastName':'Pallothu'}), 200

@app.route('/create-user', methods=['POST'])
def create_user():
    user_data = request.get_json();
    return jsonify(user_data), 201


if __name__ == '__main__':
    app.run(debug=True)
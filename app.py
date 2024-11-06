from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    "animals": [
        {
            "name": "dog",
            "sound": "bark"
        },
        {
            "name": "cat",
            "sound": "meow meow"
        }
    ]
}

@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)

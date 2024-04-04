from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import agent_utils

app = Flask(__name__)
CORS(app)


@app.route('/')
def rephrase():
    pass


@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        data = request.get_json()

        user_input = data.get('user_input')
        print(user_input)
        interest = "Farming"

        response, image_id = agent_utils.agent_run(user_input, interest)
        if image_id is None:
            return jsonify({"response": response})
        else:
            return jsonify({"response": response, "image": image_id})


@app.route('/image/<filename>')
def image(filename):
    return send_from_directory('images', filename)


@app.route('/')
def index():
    return 'Carl is not white @copyright Wisdom'


if __name__ == '__main__':
    app.run(debug=True)

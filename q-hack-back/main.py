from flask import Flask, request, jsonify
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
        interest = "Farming"

        response = agent_utils.agent_run(user_input, interest)
        return jsonify({"response": response})


@app.route('/')
def index():
    return 'Carl is not white @copyright Wisdom'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask_cors import CORS

import agent_utils

app = Flask(__name__)
CORS(app)


@app.route('/')
def rephrase():
    pass

@app.route(methods=['POST'])
def ():

    agent_utils.agent_run()
    return

@app.route('/')
def index():
    return 'Carl is not white @copyright Wisdom'


if __name__ == '__main__':
    app.run(debug=True)


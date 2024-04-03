from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Carl is not white @copyright Wisdom'


if __name__ == '__main__':
    app.run(debug=True)


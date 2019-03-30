# Import Modules:

from flask import Flask, jsonify
from flask_cors import CORS


# Create App Instance:

app = Flask(__name__)


# API Routes:

@app.route('/')
def home():

	return jsonify({'message': 'Welcome to API Home'}), 200, {'Content-Type': 'application/json'}

@app.route('/get)
def home1():

	return jsonify({'message': 'Welcome to API Get'}), 200, {'Content-Type': 'application/json'}


# Run App:

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)

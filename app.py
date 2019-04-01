# Import Modules:

from flask import Flask, jsonify
from flask_cors import CORS
import os


# Create App Instance:

app = Flask(__name__)


# API Routes:

@app.route('/')
def home():

	postgresdb_url = os.environ('DATABASE_URL', None)

	return jsonify({'message': 'Welcome to API Home', 'postgresdb_url': postgresdb_url}), 200, {'Content-Type': 'application/json'}

@app.route('/get')
def home1():

	return jsonify({'message': 'Welcome to API Get'}), 200, {'Content-Type': 'application/json'}


# Run App:

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)

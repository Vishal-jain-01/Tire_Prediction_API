from flask import Flask, request, jsonify
import numpy as np
import scipy.io
from flask_cors import CORS
import os

app = Flask(__name__)  # Corrected typo here
CORS(app)
# Load MATLAB model coefficients
mat = scipy.io.loadmat('model_coeffs.mat')  # Replace with the actual file path
beta = mat['beta'].flatten()  # Flatten to a 1D array
intercept = mat['intercept'][0][0]  # Extract the scalar value

@app.route('/')
def home():
    return "Welcome to the Tire Prediction API!"

# Define the /predict route for POST requests
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.json
        load_index = data['LoadIndex']
        width = data['Width']
        selling_price = data['SellingPrice']

        # Combine inputs into a single array
        inputs = np.array([load_index, width, selling_price])

        # Calculate prediction
        prediction = np.dot(inputs, beta) + intercept

        return jsonify({'tire_accuracy': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)


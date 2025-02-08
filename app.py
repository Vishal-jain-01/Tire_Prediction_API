from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
import scipy.io
from flask_cors import CORS
import os
import scipy.io
import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Load MATLAB model coefficients
mat = scipy.io.loadmat('model_coeffs.mat')  # Replace with the actual file path
beta = mat['beta'].flatten()  # Flatten to a 1D array
intercept = mat['intercept'][0][0]  # Extract the scalar value



# Create a simple log file
def log_prediction(data):
    with open("prediction_logs.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {data}\n")


# Home route should show the Welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for Index page (redirects from Welcome)
@app.route('/index')
def index():
    return render_template('index.html')

# Route for EntryForm page (redirects from Index)
@app.route('/entryform')
def entry_form():
    return render_template('EntryForm.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        load_index = data['LoadIndex']
        width = data['Width']
        selling_price = data['SellingPrice']

        inputs = np.array([load_index, width, selling_price])
        prediction = np.dot(inputs, beta) + intercept

         # Limit prediction between 0 and 100
        prediction = max(0, min(100, prediction))

        # Log the input and prediction
        log_data = {
            'LoadIndex': load_index,
            'Width': width,
            'SellingPrice': selling_price,
            'Prediction': prediction
        }
        log_prediction(log_data)  # Call the function to log data

        return jsonify({'tire_accuracy': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

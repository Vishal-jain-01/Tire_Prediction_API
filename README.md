Tire Accuracy Prediction

Overview

This project predicts the accuracy of tires based on various input features such as Load Index, Width, and Selling Price. The model is trained using a dataset and deployed via a Flask API, while the frontend provides an interactive UI for users to input values and get predictions.

Features

Frontend: HTML, CSS, JavaScript form for user input

Backend: Flask API for model inference

Machine Learning Model: Linear Regression with optional Ridge Regression

Deployment: Hosted on Render (or any preferred platform)

Installation & Setup

1. Clone the Repository

git clone https://github.com/Vishal-jain-01/tyre-accuracy-prediction.git
cd tyre-accuracy-prediction

2. Install Dependencies

Make sure you have Python installed, then run:

pip install -r requirements.txt

3. Run the Flask Backend

python app.py

The server will start at http://127.0.0.1:5000.

4. Open the Frontend

Simply open index.html in your browser.

API Usage

Endpoint: /predict

Method: POSTRequest Body (JSON):

{
  "LoadIndex": 85,
  "Width": 205,
  "SellingPrice": 5000
}

Response:

{
  "tire_accuracy": 82.75
}

Frontend Features

User Input Fields: Load Index, Width, Selling Price

Validation: Ensures values are within a reasonable range

Clamping Accuracy: Accuracy is constrained between 0-100% to avoid unrealistic values

Contributing

Fork the repository

Create a new branch (feature-xyz)

Commit changes (git commit -m "Added new feature")

Push to GitHub and open a Pull Request

Contact

For any queries or issues, feel free to reach out:

GitHub: Vishal-jain-01

Email: vishal112006jain@gmail.com

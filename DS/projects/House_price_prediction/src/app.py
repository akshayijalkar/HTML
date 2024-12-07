# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (Make sure the model.pkl is in the same directory or provide the full path)
model = joblib.load('F:/git/projects/DS/projects/House_price_prediction/notebooks/model.pkl')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the POST request
    data = request.get_json()

    # Convert the data into a pandas dataframe (assuming the input data is in the correct format)
    input_data = pd.DataFrame(data)

    # Make the prediction using the model
    prediction = model.predict(input_data)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load('model.pkl')

# Home route to display the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route that handles form submission
@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    location = request.form['location']  # Assuming location is a categorical feature

    # Prepare the input data in the correct format
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, location]], columns=['area', 'bedrooms', 'bathrooms', 'location'])

    # Predict using the trained model
    prediction = model.predict(input_data)

    # Return the prediction to the HTML page
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

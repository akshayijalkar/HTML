from flask import Flask, render_template, request
from model_integration import load_model, predict_house_price

app = Flask(__name__)

# Load the trained model
model = load_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    predicted_price = None
    
    if request.method == 'POST':
        try:
            area = float(request.form['area'])
            predicted_price = predict_house_price(model, area)
        except ValueError:
            predicted_price = 'Please enter a valid number for the area.'
    
    return render_template('index.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)

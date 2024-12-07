import pickle
import numpy as np

def load_model():
    # Load the trained model from file
    with open('house_price_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict_house_price(model, area):
    # Make prediction
    prediction = model.predict(np.array([[area]]))
    return prediction[0]

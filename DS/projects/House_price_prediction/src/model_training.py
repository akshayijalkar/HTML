from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
import pickle

def evaluate_model(X_train, X_test, y_train, y_test):
    # Train a Decision Tree Regressor
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Predict on test data
    y_pred = model.predict(X_test)
    
    # Evaluate model performance
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error: {mae}')
    
    # Save the model to a file
    with open('house_price_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    
    return model

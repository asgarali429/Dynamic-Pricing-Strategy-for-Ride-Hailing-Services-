from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('model.pkl')

# Vehicle type mapping function
def get_vehicle_type_numeric(vehicle_type):
    return {"Premium": 1, "Economy": 0}.get(vehicle_type, 0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        number_of_riders = int(request.form['number_of_riders'])
        number_of_drivers = int(request.form['number_of_drivers'])
        vehicle_type = request.form['vehicle_type']
        expected_ride_duration = int(request.form['expected_ride_duration'])

        # Preprocess input
        vehicle_type_numeric = get_vehicle_type_numeric(vehicle_type)
        input_data = np.array([[number_of_riders, number_of_drivers, vehicle_type_numeric, expected_ride_duration]])

        # Make prediction
        predicted_price = model.predict(input_data)[0]

        return render_template('index.html', prediction_text=f"Predicted Price: ₹{predicted_price:.2f}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

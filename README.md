# 🚗 Dynamic Pricing Strategy for Ride-Hailing Services

## 🔮 Dynamic Ride Pricing Predictor

A machine learning-powered Flask application that predicts dynamic ride pricing based on real-time demand, supply, and vehicle type.

---

## 📌 Problem Statement

Ride-sharing companies often face challenges in setting dynamic pricing. Prices should adapt based on rider demand, driver availability, vehicle type, and expected ride duration. This project builds a model to help predict ride cost dynamically.

---

## 🛠 Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- Plotly (for EDA and visualizations)
- Joblib (for model persistence)

---

## 📁 Project Structure

Dynamic Pricing Strategy for Ride-Hailing Services /
├── app.py # Flask web app
├── model.pkl # Trained ML model
├── templates/
│ └── index.html # Frontend form
├── dynamic_pricing_analysis.ipynb # EDA + model training
├── requirements.txt
└── README.md

---

## 📈 Exploratory Data Analysis

- Correlation Matrix Heatmap
- Scatter plots for `Expected Ride Duration` vs `Historical Cost`
- Box plots for `Vehicle Type` vs `Cost`
- Demand & Supply multipliers
- Profitability pie chart

---

## 🤖 Machine Learning

- Features: Number of Riders, Number of Drivers, Vehicle Type, Expected Ride Duration
- Target: Adjusted Ride Cost
- Model: RandomForestRegressor
- Evaluation: R² Score, RMSE

---

## 🧪 Model Performance

- **R² Score:** *0.86*  
- **RMSE:** *176.38*

---

## 💻 How to Run the App

1. Clone the repo or upload files
2. Make sure `model.pkl` is in the same directory as `app.py`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Run the Flask app:

python app.py

Go to http://127.0.0.1:5000 in your browser.


## 🖼️ Screenshot
![image](https://github.com/user-attachments/assets/f6a40848-f751-4923-a5c5-0b0e19b325cc)



## 👤 Author
ASGARALI MALPARA

GitHub --> https://github.com/asgarali429

LinkedIn -->www.linkedin.com/in/asgarali-malpara-5a78462a9


## ✨ Features
Predicts ride cost based on user input

Differentiates between Economy and Premium vehicles

Fully interactive web UI with form submission

Real-world data preprocessing pipeline in notebook


## 🔮 Future Improvements
Deploy using heroku

Add historical trends in UI

Store user input history and predictions



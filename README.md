# ❤️ Heart Disease Prediction App

A simple and interactive web app that predicts whether a person is at **high or low risk** of heart disease based on medical parameters, using a Machine Learning model built in Python.

[Click here to try the app](https://heart-disease-app-9tjbz6xoedfgzqbrjaekgs.streamlit.app/) <!-- 🔁 Replace with actual app URL -->

---

## 🚀 Features

- 🔢 Predicts heart disease risk using clinical data
- 📈 Uses a trained machine learning model
- 🧠 Built with Streamlit for fast and interactive UI
- 💾 Deployable and lightweight
- 📤 Export predictions to CSV

---

## 🧪 Inputs Used for Prediction

The app uses the following 13 features from the [Cleveland Heart Disease dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease):

| Feature | Description |
|--------|-------------|
| age | Age of the patient |
| sex | Gender (1 = male, 0 = female) |
| cp | Chest pain type (0–3) |
| trestbps | Resting blood pressure |
| chol | Serum cholesterol |
| fbs | Fasting blood sugar > 120 mg/dl |
| restecg | Resting electrocardiographic results |
| thalach | Max heart rate achieved |
| exang | Exercise-induced angina |
| oldpeak | ST depression |
| slope | Slope of the ST segment |
| ca | Major vessels (0–3) colored by fluoroscopy |
| thal | Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect) |

---

## 🤖 Model Details

- 📚 Algorithm: Logistic Regression (or your actual model)
- 🧠 Trained on: `processed.cleveland.data`
- 🛠 Libraries used: `scikit-learn`, `pandas`, `numpy`, `joblib`

---

## 📸 Screenshot

![App Screenshot](s_lit.png) 
### 📊 Prediction Output
![Prediction Result](s_lit2.png)

### 📤 CSV Export
![Export Button](s_lit4.png)
---

## 🛠 Setup & Run Locally

```bash
# Clone the repository
git clone https://github.com/Ankit2729/heart-disease-app.git
cd heart-disease-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

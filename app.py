
import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model and scaler
model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Disease Predictor",page_icon = "❤️", layout = "centered")

st.sidebar.title("ℹ️ About")
st.sidebar.info("""
This app predicts the likelihood of heart disease using several health indicators.
⚠️ This tool is for educational purposes only and not a medical diagnosis.
""")

st.markdown("<h1 style='text-align: center; color: red;'>❤️ Heart Disease Risk Prediction </h1>",unsafe_allow_html=True)

st.header("📝Enter Patient Details")
col1,col2 = st.columns(2)

with col1:
  age = st.slider("age",20,100,50)
  sex = st.radio("sex",  ["Female", "Male"])
  cp = st.selectbox("Chest Pain Type",["Typical Angina (0)","Atypical Angina (1)","Non-anginal Pain (2)","Asymptomatic (3)"])
  trestbps = st.number_input("Resting BP (mm Hg)", value=120)
  chol = st.number_input("Serum Cholestoral (mg/dl)", value=200)
  fbs = st.radio("Fasting Blood Sugar > 120 mg/dl",["No (0)","Yes (1)"])

with col2:
  restecg = st.radio("Rest ECG Results",["Normal (0)","ST-T Wave Abnormaliy (1)","LV Hypertrophy (2)"])
  thalach = st.number_input("Max Heart Rate Achieved",value=150)
  exang = st.radio("Exercise-Induced Angina",["No (0)", "Yes (1)"])
  oldpeak = st.number_input("ST Depression Induced by Exercise",value=1.0)
  slope = st.selectbox("Slope of Peak Exercise ST",["Unsloping (0)","Flat (1)","Downslopping (2)"])
  ca = st.selectbox("Major Vessels Colored by Fluoroscopy (0-3)",[0,1,2,3])
  thal = st.selectbox("Thalassemia ",["Normal (1)","Fixed Defect (2)","Reversible Defect (3)"])

inp = np.array([[age,
    1 if sex == "Male" else 0,
    int(cp[cp.find("(")+1:cp.find(")")]),
    trestbps,
    chol,
    1 if fbs == "Yes (1)" else 0,
    int(restecg[restecg.find("(")+1:restecg.find(")")]),
    thalach,
    1 if exang == "Yes (1)" else 0,
    oldpeak,
    int(slope[slope.find("(")+1:slope.find(")")]),
    ca,
    int(thal[thal.find("(")+1:thal.find(")")])
]])

input_labels = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
inp_df = pd.DataFrame(inp, columns=input_labels)

display_df = inp_df.T.reset_index()
display_df.columns = ["Feature","Value"]
display_df["Value"] = display_df["Value"].apply(lambda x: int(x) if x==int(x) else round(x,2))

with st.expander("🔍 View Input Details"):
    st.dataframe(display_df.style.set_properties(**{'text-align': 'left','border-color': 'gray'}))

if st.button("🚀 Predict"):
    scaled = scaler.transform(inp_df)
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🔎 Prediction Result:")
        if prediction == 1:
            st.markdown("### 🫀 **High Risk of Heart Disease Detected!**")
            st.error("Please consult a healthcare professional.")
        else:
            st.markdown("### ✅ **Low Risk of Heart Disease**")
            st.success("Keep maintaining a healthy lifestyle!")

    with col2:
        st.subheader("📊 Confidence")
        st.progress(probability)
        prob_text = f"**{probability:.2f}**"
        if probability > 0.7:
            st.markdown(f"🟥 {prob_text}")
        elif probability > 0.4:
            st.markdown(f"🟨 {prob_text}")
        else:
            st.markdown(f"🟩 {prob_text}")



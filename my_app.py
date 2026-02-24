
# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # --------------------------
# # Load model & features
# # --------------------------
# model = joblib.load("my_xgb_model.pkl")
# features = joblib.load("model_features.pkl")

# st.set_page_config(page_title="Credit Risk Predictor", layout="centered")
# st.title("Single Customer Credit Risk Prediction")

# st.write("Enter customer loan details below to predict default risk.")

# # --------------------------
# # User Inputs
# # --------------------------
# Total_Amount = st.number_input("Total Loan Amount", min_value=0.0, value=5000.0)
# Total_Amount_to_Repay = st.number_input("Total Amount to Repay", min_value=0.0, value=6000.0)
# duration = st.number_input("Loan Duration (days)", min_value=1, value=30)
# # Amount_Funded_By_Lender = st.number_input("Amount Funded by Lender", min_value=0.0, value=5000.0)
# Lender_portion_Funded = st.number_input("Lender Portion Funded (%)", min_value=0.0, max_value=100.0, value=100.0)
# # Lender_portion_to_be_repaid = st.number_input("Lender Portion to be Repaid", min_value=0.0, value=6000.0)

# New_versus_Repeat = st.selectbox("Customer Type", ["New", "Repeat"])
# loan_type = st.selectbox("Loan Type", ["Short-Term", "Medium-Term", "Long-Term"])

# # --------------------------
# # Feature Engineering
# # --------------------------
# repayment_ratio = Total_Amount_to_Repay / Total_Amount if Total_Amount > 0 else 0
# amount_due_per_day = Total_Amount_to_Repay / duration if duration > 0 else 0

# log_Total_Amount = np.log1p(Total_Amount)
# log_Total_Amount_to_Repay = np.log1p(Total_Amount_to_Repay)
# log_Amount_Funded_By_Lender = np.log1p(Amount_Funded_By_Lender)
# log_Lender_portion_to_be_repaid = np.log1p(Lender_portion_to_be_repaid)

# New_versus_Repeat_encoded = 1 if New_versus_Repeat == "Repeat" else 0
# loan_type_encoded = 0 if loan_type == "Short-Term" else 1 if loan_type == "Medium-Term" else 2

# # --------------------------
# # Create base feature dict
# # --------------------------
# input_dict = {
#     "Total_Amount": Total_Amount,
#     "Total_Amount_to_Repay": Total_Amount_to_Repay,
#     "duration": duration,
#     #"Amount_Funded_By_Lender": Amount_Funded_By_Lender,
#     "Lender_portion_Funded": Lender_portion_Funded,
#     #"Lender_portion_to_be_repaid": Lender_portion_to_be_repaid,
#     "repayment_ratio": repayment_ratio,
#     "amount_due_per_day": amount_due_per_day,
#     "log_Total_Amount": log_Total_Amount,
#     "log_Total_Amount_to_Repay": log_Total_Amount_to_Repay,
#     "log_Amount_Funded_By_Lender": log_Amount_Funded_By_Lender,
#     "log_Lender_portion_to_be_repaid": log_Lender_portion_to_be_repaid,
#     "New_versus_Repeat": New_versus_Repeat_encoded,
#     "loan_type": loan_type_encoded
# }

# # --------------------------
# # Fill missing features with 0
# # --------------------------
# for col in features:
#     if col not in input_dict:
#         input_dict[col] = 0

# input_data = pd.DataFrame([input_dict])[features]

# # --------------------------
# # Risk tier function
# # --------------------------
# def assign_risk_level(prob):
#     if prob < 0.2:
#         return "LOW RISK"
#     elif prob < 0.5:
#         return "MEDIUM RISK"
#     elif prob < 0.8:
#         return "HIGH RISK"
#     else:
#         return "VERY HIGH RISK"

# # --------------------------
# # Prediction
# # --------------------------
# if st.button("Predict Risk"):
#     prob = model.predict_proba(input_data)[0][1]
#     pred = int(prob >= 0.5)
#     risk_level = assign_risk_level(prob)

#     st.subheader("Prediction Result")
#     st.write(f"**Default Probability:** {prob:.2%}")
#     st.write(f"**Predicted Default:** {'Yes' if pred == 1 else 'No'}")
#     st.write(f"**Risk Tier:** {risk_level}")

#     if risk_level in ["HIGH RISK", "VERY HIGH RISK"]:
#         st.error("⚠️ This customer is high risk. Consider stricter approval or additional checks.")
#     else:
#         st.success("✅ This customer is low to medium risk.")

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --------------------------
# Load model & features
# --------------------------
model = joblib.load("my_xgb_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="Credit Risk Predictor", layout="centered")
st.title("Single Customer Credit Risk Prediction")

st.write("Enter customer loan details below to predict default risk.")

# --------------------------
# User Inputs
# --------------------------
Total_Amount = st.number_input("Total Loan Amount", min_value=0.0, value=5000.0)
Total_Amount_to_Repay = st.number_input("Total Amount to Repay", min_value=0.0, value=6000.0)
duration = st.number_input("Loan Duration (days)", min_value=1, value=30)

# --------------------------
# Auto-assign lender values (Hidden from UI)
# Model was trained assuming 100% lender funding
# --------------------------
Lender_portion_Funded = 100.0
Amount_Funded_By_Lender = Total_Amount
Lender_portion_to_be_repaid = Total_Amount_to_Repay

New_versus_Repeat = st.selectbox("Customer Type", ["New", "Repeat"])
loan_type = st.selectbox("Loan Type", ["Short-Term", "Medium-Term", "Long-Term"])

# --------------------------
# Feature Engineering
# --------------------------
repayment_ratio = Total_Amount_to_Repay / Total_Amount if Total_Amount > 0 else 0
amount_due_per_day = Total_Amount_to_Repay / duration if duration > 0 else 0

log_Total_Amount = np.log1p(Total_Amount)
log_Total_Amount_to_Repay = np.log1p(Total_Amount_to_Repay)
log_Amount_Funded_By_Lender = np.log1p(Amount_Funded_By_Lender)
log_Lender_portion_to_be_repaid = np.log1p(Lender_portion_to_be_repaid)

New_versus_Repeat_encoded = 1 if New_versus_Repeat == "Repeat" else 0
loan_type_encoded = 0 if loan_type == "Short-Term" else 1 if loan_type == "Medium-Term" else 2

# --------------------------
# Create base feature dict
# --------------------------
input_dict = {
    "Total_Amount": Total_Amount,
    "Total_Amount_to_Repay": Total_Amount_to_Repay,
    "duration": duration,
    "Amount_Funded_By_Lender": Amount_Funded_By_Lender,
    "Lender_portion_Funded": Lender_portion_Funded,
    "Lender_portion_to_be_repaid": Lender_portion_to_be_repaid,
    "repayment_ratio": repayment_ratio,
    "amount_due_per_day": amount_due_per_day,
    "log_Total_Amount": log_Total_Amount,
    "log_Total_Amount_to_Repay": log_Total_Amount_to_Repay,
    "log_Amount_Funded_By_Lender": log_Amount_Funded_By_Lender,
    "log_Lender_portion_to_be_repaid": log_Lender_portion_to_be_repaid,
    "New_versus_Repeat": New_versus_Repeat_encoded,
    "loan_type": loan_type_encoded
}

# --------------------------
# Fill missing features with 0
# --------------------------
for col in features:
    if col not in input_dict:
        input_dict[col] = 0

input_data = pd.DataFrame([input_dict])[features]

# --------------------------
# Risk tier function
# --------------------------
def assign_risk_level(prob):
    if prob < 0.2:
        return "LOW RISK"
    elif prob < 0.5:
        return "MEDIUM RISK"
    elif prob < 0.8:
        return "HIGH RISK"
    else:
        return "VERY HIGH RISK"

# --------------------------
# Prediction
# --------------------------
if st.button("Predict Risk"):
    prob = model.predict_proba(input_data)[0][1]
    pred = int(prob >= 0.5)
    risk_level = assign_risk_level(prob)

    st.subheader("Prediction Result")
    st.write(f"**Default Probability:** {prob:.2%}")
    st.write(f"**Predicted Default:** {'Yes' if pred == 1 else 'No'}")
    st.write(f"**Risk Tier:** {risk_level}")

    if risk_level in ["HIGH RISK", "VERY HIGH RISK"]:
        st.error("⚠️ This customer is high risk. Consider stricter approval or additional checks.")
    else:
        st.success("✅ This customer is low to medium risk.")
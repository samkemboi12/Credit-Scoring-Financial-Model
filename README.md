# Credit-Scoring-Financial-Model
This is a project that deals with risk management in financial institutions regarding lending to its customers. It develops a credit scoring system that predicts whether a customer will default a loan. It ensures profitability since banks make informed lending decisions improving profitability and reducing financial losses.

This project covers data preprocessing, feature engineering, model training, hyperparameter tuning, ensemble learning, evaluation, and live deployment via Streamlit.

# Business Understanding
Financial institutions, such as banks and microfinance organizations, regularly face the challenge of lending money to customers while minimizing the risk of loan defaults. Every loan carries a certain level of risk: some customers repay on time, while others may default due to financial constraints, poor credit history, or unforeseen circumstances. Efficiently managing this risk is critical for the profitability and sustainability of the institution. Credit scoring is all about assessing the creditworthiness of loan applicants. The goal is to predict the likelihood that a customer or a business will default on a loan so that the bank can make informed lending decisions.

# Business Problem
Wonders2015 Finance Solutions  has a pool of customers individual and Small and Medium sized Enterprises (SMEs) applying for loans.
Not all applicants have the same repayment capacity.
Wonders2015 Finance uses traditional loan approval process which relies on manual assessments, subjective judgment, or incomplete evaluation of a customer’s financial history.
The process is inconsistent, leading to Lending to high risk customers welcoming losses and rejecting low risk customers which leads to losing business opportunities

We need a data driven model that predicts the probability of default for each applicant either as an individual or SMEs.

# Project Objective
The main objective of this project is to develop a data-driven credit scoring system that predicts the likelihood of a customer defaulting on a loan. This model will help the bank make informed, consistent, and fair lending decisions, ultimately improving risk management and profitability.
This the projects matters because of the following reasons.

Improve default prediction accuracy.

Risk management- Reduce financial losses from loan defaults.

Regulatory compliance -Banks must comply with financial regulations on lending and risk.

Profitability - Proper credit scoring allows offering loans to low-risk customers while charging appropriate interest for higher risk ones.

Customer fairness - Ensures decisions are data driven, consistent, and unbiased.

Provide interpretable risk tiers for business users

# Key Deliverables:
Data understanding and cleaning: Understand data fields, handle missing values, and correct inconsistencies.

Feature engineering: Create meaningful variables such as Financial Ratios and Transformations and Temporal Features from dates

Exploratory analysis: Identify factors that influence default risk,such as loan type, default history and so on

Model development: Build ML models, LightGBM, XGBoost and Catboost to predict defaults.

Model evaluation: Use metrics F1 Score, AUC-ROC, KS, Classification report and confusion matrix.

Business insights: Explain which factors most affect default risk.

Deployment-ready solution: Provide predictions or scorecards for new applicants.

Note that , this project addresses a highly imbalanced dataset, applies group-aware cross-validation, and deploys a real-time scoring application for individual customers

# Explonatory Data Analysis
## Distribution of Target

<img width="513" height="333" alt="download" src="https://github.com/user-attachments/assets/fde8f36b-9d86-4168-a7db-3bec1703ec54" />

From the plot and percentages, it is clear that the dataset is highly imbalanced. The majority of customers repay their loans on time (target = 0), while only a small fraction default (target = 1). This imbalance is important to note because it can affect model training since models may be biased toward predicting the majority class if special care is not taken, such as using class weights or resampling techniques.
## Examine Loan type vs default rate
<img width="960" height="443" alt="download" src="https://github.com/user-attachments/assets/124b92b8-879f-4554-9149-b3febbded40e" />

## Examine New vs Repeat loans
<img width="402" height="266" alt="download" src="https://github.com/user-attachments/assets/06b3ed53-5cbf-420c-a41d-06cb6c8c9fb5" />

## Feature Engineering

Engineered business driven features to capture borrower behavior, loan structure, and repayment risk.

* **Customer-Level Aggregates:**
  Computed each customer’s mean and median repayment amounts to summarize their typical loan burden and historical behavior.

* **Temporal Features:**
  Extracted loan dates into year, month, day, and weekday, and calculated loan term (in days) to capture seasonal patterns, duration risk, and timing effects.

* **Financial Ratios & Transformations:**
  Created repayment ratios, daily repayment burden, and applied log transformations to normalize skewed financial variables and improve model stability.

* **Behavioral Deviations:**
  Measured how each loan compares to a customer’s historical average to detect unusually risky borrowing behavior.

* **Engineered Risk Score:**
  Built a transparent, rule-based risk scoring system using financial stress indicators, loan characteristics, and customer status, mapping borrowers into intuitive tiers: **GOOD, MEDIUM, HIGH, VERY HIGH, EXTREME**.

These features significantly improved model performance while ensuring interpretability for business and stakeholder use.

## Modelling
| Fold        | Default Precision | Default Recall | Default F1 | ROC-AUC    | PR-AUC     |
| ----------- | ----------------- | -------------- | ---------- | ---------- | ---------- |
| 1           | 0.66              | 0.83           | 0.74       | 0.9924     | 0.8568     |
| 2           | 0.74              | 0.78           | 0.76       | 0.9949     | 0.8561     |
| 3           | 0.72              | 0.80           | 0.75       | 0.9905     | 0.8452     |
| 4           | 0.71              | 0.81           | 0.75       | 0.9942     | 0.8783     |
| **Average** | **0.71**          | **0.81**       | **0.75**   | **0.9930** | **0.8591** |

## Deployment
The final model was deployed using Streamlit to provide a simple, interactive web application for real-time credit risk assessment at the individual customer level.

Key deployment features:

Users input borrower and loan details manually (no CSV upload required).

The app preprocesses inputs using the same feature engineering pipeline as training.

The trained model generates a default probability and assigns a risk tier (GOOD → EXTREME).

Results are displayed instantly, making the tool suitable for loan officers, risk analysts, and decision-makers.

This deployment demonstrates how machine learning can be translated into a practical, business-ready decision support system, bridging data science and real-world credit operations.
## How to use this Project
* Clone this Repo.
* Launch the App
* Run the Streamlit app from your terminal: streamlit run my_app.py
*Input Borrower Details:<br>
Enter individual customer loan and personal information in the input fields, such as:<br>
Loan amount, repayment amount, loan term<br>
Disbursement and due dates<br>
New or repeat customer<br>
Any other required financial metrics<br>

* View Predictions

* The app calculates the probability of default for the customer.

* It assigns a risk tier (GOOD, MEDIUM, HIGH, VERY HIGH, EXTREME) based on the engineered risk score.

* Make Decisions
Use the probability and risk tier to:<br>
Approve or reject loans<br>
Adjust interest rates or repayment schedules<br>
Identify high-risk customers for closer monitoring<br>

* For New Customers
You can enter values manually and instantly get the predicted risk, without needing historical data files.
## Contact
For any inquiries please contact me through email: samkemboi201@gmail.com

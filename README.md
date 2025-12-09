# Credit-Scoring-Financial-Model
This is a project that deals with risk management in financial institutions regarding lending to its customers. It develops a credit scoring system that predicts whether a customer will default a loan. It ensures profitability since banks make informed lending decisions improving profitability and reducing financial losses.
Business Understanding
Financial institutions, such as banks and microfinance organizations, regularly face the challenge of lending money to customers while minimizing the risk of loan defaults. Every loan carries a certain level of risk: some customers repay on time, while others may default due to financial constraints, poor credit history, or unforeseen circumstances. Efficiently managing this risk is critical for the profitability and sustainability of the institution. Credit scoring is all about assessing the creditworthiness of loan applicants. The goal is to predict the likelihood that a customer or a business will default on a loan so that the bank can make informed lending decisions.

# Business Problem
Evercrest Bank has a pool of customers individual and Small and Medium sized Enterprises (SMEs) applying for loans.
Not all applicants have the same repayment capacity.
Evercrest Bank uses traditional loan approval process which relies on manual assessments, subjective judgment, or incomplete evaluation of a customer’s financial history.
The process is inconsistent, leading to Lending to high risk customers welcoming losses and rejecting low risk customers which leads to losing business opportunities

We need a data driven model that predicts the probability of default for each applicant either as an individual or SMEs.

# Project Objective
The main objective of this project is to develop a data-driven credit scoring system that predicts the likelihood of a customer defaulting on a loan. This model will help the bank make informed, consistent, and fair lending decisions, ultimately improving risk management and profitability.
This the projects matters because of the following reasons.

Risk management- Reduce financial losses from loan defaults.

Regulatory compliance -Banks must comply with financial regulations on lending and risk.

Profitability - Proper credit scoring allows offering loans to low-risk customers while charging appropriate interest for higher risk ones.

Customer fairness - Ensures decisions are data driven, consistent, and unbiased.

# Key Deliverables:
Data understanding and cleaning: Understand data fields, handle missing values, and correct inconsistencies.

Feature engineering: Create meaningful variables such as Debt To Income ratio, Develop Risk Score, Rejected Contract History.Credit-to-Annuity Ratio,Employment Stability,Default Rate by Income Source and Occupation

Exploratory analysis: Identify factors that influence default risk,such as occupation, age, employment, DTI, default history and so on

Model development: Build ML models e.g., LightGBM, Random Forest) to predict defaults.

Model evaluation: Use metrics like AUC-ROC, KS, Classification report and confusion matrix.

Business insights: Explain which factors most affect default risk.

Deployment-ready solution: Provide predictions or scorecards for new applicants.

# Explonatory Data Analysis
## Distribution of Target
Target is 0 (Non Defaulters) = 91.9 %
          1 (Defaulters ) = 8.1 %
          <img width="245" height="231" alt="download" src="https://github.com/user-attachments/assets/daf5024e-8ca3-4416-b5b9-735abe96d811" />
## Explore Employment Risk Patterns
### Is there a Relationship between years of Employment and Loan Default
<img width="615" height="358" alt="download" src="https://github.com/user-attachments/assets/19722391-3a49-417e-bda4-62f337b9a6e2" />

Yes, Analysis shows that applicants with longer employment history have lower default risk.
Shorter employment duration is associated with higher probability of default, indicating that job stability is an important factor in credit risk assessment.”

## Explore Age Risk Patterns
### Is there a Relationship between Age of customers and Loan Default
<img width="615" height="358" alt="download" src="https://github.com/user-attachments/assets/75048d7c-92b1-4501-9bc7-04ef161e08cd" />

Analysis shows that default risk decreases with age.
<br>Younger borrowers are more likely to default, while older borrowers tend to be more financially stable and reliable in meeting credit obligations.

## Engineered Risk score
Created a risk score to estimate how risky a client is. First, I looked at key indicators like **debt levels**, **loan size compared to income**, **employment stability**, and **past loan rejections**. 
<br>For each indicator, I marked whether it was risky or not. 
<br>Then, I added up these marks to get a total risk score. 
<br>Finally, I converted this score into a simple risk level category—like ;
<br>GOOD,
<br>MEDIUM, 
<br>HIGH, 
<br>VERY HIGH, 
<br>or EXTREME ,so it’s easy to understand and use in decisions.
<br>For example, a client with low Debt to Income ratio (DIT), stable employment, and no past rejections would be classified as GOOD risk. On the other hand, a client with high DIT, low job stability, and several past rejections would be EXTREME risk.


I have created a function called  calculate_risk_level  in the notebook to test the risk score
## Example 1
print(calculate_risk_level(dti=0.15, credit_annuity=0.2, employment=10, rejections=0))
### Output: 'GOOD'

## Example 2
print(calculate_risk_level(dti=0.35, credit_annuity=0.25, employment=1, rejections=9))
### Output: 'EXTREME'





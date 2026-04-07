# Credit Risk Analysis & Loan Behavior Dashboard (Power BI and python)

## Project Overview

This project focuses on analyzing **customer credit risk, loan behavior, and default patterns** using cleaned and transformed financial data.

The dataset initially contained missing values, invalid entries, and inconsistencies, which were cleaned and prepared before building interactive dashboards in Power BI.

## Objectives

* Analyze customer credit risk distribution
* Understand loan behavior across different customer segments
* Identify patterns leading to loan defaults
* Build dashboards for decision-making in financial institutions

## Tools & Technologies

* Power BI (Power Query + Dashboards)
* Excel / CSV Dataset
* Data Cleaning Techniques
* DAX (Calculated Columns & Measures)
  
## Data Cleaning & Preparation

### Cleaning Steps Performed

* Cleaned and standardized **Customer_ID**
* Handled missing values (Income, Credit Score, Loan Amount)
* Removed duplicate records
* Fixed invalid values (negative income, loan amounts)
* Converted columns into correct data types
* Standardized categorical fields (employment, segments, etc.)

## Derived Columns & Measures

* Debt-to-Income Ratio (DTI)
* Risk Category (Low / Medium / High)
* Default Rate (%)
* Risk Score
* Income Groups
* Loan Segments

## Dashboards Created

### 1. Credit Risk Overview

* KPIs: Total Customers, Avg Credit Score, Default Rate
* Default vs Non-default distribution
* Risk category analysis

### 2. Loan Analysis Dashboard

* Total & Average Loan Amount
* Loan distribution across segments

### 3. Credit Score Analysis

* Credit score distribution
* Credit score vs default relationship

### 4. Income vs Default Dashboard

* Income impact on loan default
* Income vs loan scatter analysis

### 5. DTI (Debt-to-Income) Analysis

* Financial burden evaluation
* Default rate based on DTI

### 6. Employment & Credit Risk

* Default rate across employment categories
* Loan distribution by employment

### 7. Customer Segmentation

* Risk-based segmentation
* High-risk customer identification

### 8. Risk Scoring Dashboard (Advanced)

* Custom Risk Score:
  Risk Score = (0.4 × DTI) + (0.3 × Loan Amount) + (0.3 × Default History)

### 9. Default Prediction Dashboard

* Correlation analysis
* Key factors influencing default

### 10. Executive Summary Dashboard

* Overall KPIs and trends
* High-risk customer tracking

##  Dashboard Screenshots

<img width="1920" height="1080" alt="Screenshot (136)" src="https://github.com/user-attachments/assets/04c53de7-12b1-4776-838d-d6bb75650957" />
<img width="1920" height="1080" alt="Screenshot (135)" src="https://github.com/user-attachments/assets/5cb250dd-f932-4190-b6cd-1e9540b4a399" />
<img width="1920" height="1080" alt="Screenshot (134)" src="https://github.com/user-attachments/assets/78066989-c01f-4469-87b5-8ccf5354eb5e" />
<img width="1920" height="1080" alt="Screenshot (133)" src="https://github.com/user-attachments/assets/413bd245-efd6-4387-bd7d-c47cb2eda558" />
<img width="1920" height="1080" alt="Screenshot (132)" src="https://github.com/user-attachments/assets/7d21eb6f-1716-4dcb-b538-cbf9d110c6a4" />

## Project Files

* po5.pbix (Power BI file)
* Raw dataset
* Cleaned dataset
* Screenshots

##  Key Insights

* Customers with **low credit scores** show higher default rates
* High **DTI ratios** significantly increase financial risk
* Certain **income groups** are more prone to default
* Loan amount and repayment capacity are strongly correlated
* High-risk customers can be identified using custom risk scoring

## Learning Outcomes

* Data cleaning using Power Query
* Financial data analysis and interpretation
* Risk modeling and segmentation
* Building interactive dashboards in Power BI
* Applying business logic using DAX


##  Future Enhancements

* Add machine learning-based default prediction
* Integrate real-time financial datasets
* Improve risk scoring model with more parameters

This project demonstrates my ability to analyze financial data, identify risk patterns, and build dashboards for decision-making in banking and finance.

Credit Risk Prediction using Machine Learning

##  Project Overview

This project focuses on predicting whether a customer is likely to **default on a loan** using Machine Learning techniques.
The model analyzes customer financial and behavioral data to assist banks and financial institutions in making better lending decisions.

## Objective

* Identify high-risk customers
* Reduce financial loss due to loan defaults
* Build a reliable ML model for credit risk analysis

## ️ Technologies Used

* Python
* Pandas & NumPy (Data Processing)
* Scikit-learn (Machine Learning)
* Matplotlib & Seaborn (Visualization)

## Project Workflow

1. **Data Collection**

   * Loaded dataset from Excel file

2. **Data Cleaning**

   * Handled missing values
   * Removed invalid entries ("error")
   * Converted columns to numeric format

3. **Data Preprocessing**

   * Filled missing values using mean/mode
   * Encoded categorical variables
   * Feature scaling using StandardScaler

4. **Feature Selection**

   * Selected relevant features for prediction
   * Defined target variable (Default_Status)

5. **Model Building**

   * Logistic Regression
   * Decision Tree Classifier
   * Random Forest Classifier

6. **Model Evaluation**

   * Accuracy Score
   * Confusion Matrix
   * Classification Report

7. **Visualization**

   * Confusion Matrix Heatmaps
   * Model Accuracy Comparison Graph
   * Feature Importance Analysis

## Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 86%      |
| Decision Tree       | 99%      |
| Random Forest       | 99%      |

## Key Insights

* Random Forest and Decision Tree achieved the highest accuracy (~99%)
* Logistic Regression performed well but slightly lower (~86%)
* Feature importance analysis helped identify key factors affecting loan default

##  Limitations

* High accuracy may indicate possible overfitting
* Further validation like cross-validation can improve reliability

## Future Improvements

* Deploy model using Streamlit (Web App)
* Add real-time prediction system
* Use larger and more realistic datasets
* Apply advanced models like XGBoost

##  Project Structure

Credit-Risk-ML/
│
├── data/
├── src/
│   └── credit_model.py
├── outputs/
└── README.md

## Use Case

This project can be used by:

* Banks
* Financial institutions
* Loan approval systems

## Author

Manasa M
Aspiring Data Analyst | Machine Learning Enthusiast


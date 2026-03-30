# Credit Risk Analysis & Loan Behavior Dashboard (Power BI)

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
  

✨ This project demonstrates my ability to analyze financial data, identify risk patterns, and build dashboards for decision-making in banking and finance.



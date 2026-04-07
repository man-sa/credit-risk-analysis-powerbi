# ===========================
# CREDIT RISK ML PROJECT
# ===========================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ===========================
# 2. Load Dataset
# ===========================
df = pd.read_excel("../data/credit-risk-cleaned dataset.xlsx")

# ===========================
# 3. Data Cleaning
# ===========================
df.replace("error", np.nan, inplace=True)

cols = ['Age', 'Income', 'Credit_Score', 'Loan_Amount',
        'Loan_Term', 'Existing_Loans', 'Debt_to_Income_Ratio']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.fillna(df.mean(numeric_only=True), inplace=True)

# Fix categorical missing values
df['Employment_Status'] = df['Employment_Status'].fillna(df['Employment_Status'].mode()[0])
df['Payment_History'] = df['Payment_History'].fillna(df['Payment_History'].mode()[0])
df['Collateral'] = df['Collateral'].fillna(df['Collateral'].mode()[0])

# Remove unwanted column
if 'Customer_ID' in df.columns:
    df.drop('Customer_ID', axis=1, inplace=True)

# Fix target
df['Default_Status'] = pd.to_numeric(df['Default_Status'], errors='coerce')
df['Default_Status'] = df['Default_Status'].fillna(0)
df = df[df['Default_Status'] != -1]

# ===========================
# 4. Encoding
# ===========================
le = LabelEncoder()

df['Employment_Status'] = le.fit_transform(df['Employment_Status'])
df['Payment_History'] = le.fit_transform(df['Payment_History'])
df['Collateral'] = le.fit_transform(df['Collateral'])

# ===========================
# 5. Feature Selection
# ===========================
X = df.drop('Default_Status', axis=1)
y = df['Default_Status'].astype(int)

# Convert ALL remaining text columns automatically
X = pd.get_dummies(X)
# ===========================
# 6. Scaling
# ===========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ===========================
# 7. Train-Test Split
# ===========================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ===========================
# MODEL 1: Logistic Regression
# ===========================
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("\n--- Logistic Regression ---")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

# Heatmap
plt.figure()
cm_lr = confusion_matrix(y_test, y_pred_lr)
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Default','Default'],
            yticklabels=['No Default','Default'])
plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ===========================
# MODEL 2: Decision Tree
# ===========================
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

print("\n--- Decision Tree ---")
print("Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))

# Heatmap
plt.figure()
cm_dt = confusion_matrix(y_test, y_pred_dt)
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Greens',
            xticklabels=['No Default','Default'],
            yticklabels=['No Default','Default'])
plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ===========================
# MODEL 3: Random Forest
# ===========================
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("\n--- Random Forest ---")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Heatmap
plt.figure()
cm_rf = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Reds',
            xticklabels=['No Default','Default'],
            yticklabels=['No Default','Default'])
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ===========================
# 8. Accuracy Comparison Graph
# ===========================
models = ['Logistic Regression', 'Decision Tree', 'Random Forest']
accuracies = [
    accuracy_score(y_test, y_pred_lr),
    accuracy_score(y_test, y_pred_dt),
    accuracy_score(y_test, y_pred_rf)
]

plt.figure()
plt.bar(models, accuracies)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()

# ===========================
# 9. Feature Importance
# ===========================
importance = rf.feature_importances_

plt.figure()
plt.barh(X.columns, importance)
plt.title("Feature Importance")
plt.show()
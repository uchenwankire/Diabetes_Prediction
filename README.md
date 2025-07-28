# Diabetes_Prediction
## Problem Statament
Diabetes poses significant health risks to
Stark Health’s patients, and also
financial challenges. Current methods
for early detection at Stark Health Clinic
lack precision, leading to missed
opportunities for timely interventions. 
## Rationale of Project
By accurately predicting diabetes risk
through advanced machine learning,
Stark Health Clinic can improve patient
care, reduce long-term costs, and take a
proactive role in combating diabetes.
## Project Objective
This project aims to develop a robust diabetes prediction model to
accurately identify individuals at risk of developing diabetes, allowing for timely
and targeted preventive measures.

This initiative will empower Stark Health to enhance patient outcomes,
reduce the burden on healthcare resources, and play a proactive role in
combating diabetes.
## Project Processes
1. Data Preparation: 
Checked for missing data and found non, removed duplicate data, standardized date format
2. Exploratory Data Analysis (EDA) in Python:  
    (a) Visualize relationships between the target and some key features 
    (b) Explore correlations (c) Conduct univariate,bivariate,and multivariate analysis
    Tools: Python, NumPy, Pandas, MatPlotLib/Seaborn, SciKit Learn, Jupyter Notebook.
3. Feature Engineering and Model Training: 
    This include: label encoding of categorical data, splitting the dataset into dependent and independent features,
    perform traind and test split of 80%/20% and normalize imbalance dataset using MinMax Scaller 
    and Supervised Machine Learning to train the Model.
## Model Evalaution
After training the model with various algorithms which include: Logistic Regression, SGDClassifier,	K-Nearest Neighbors, 
Decision Tree, Random Forest, AdaBoost, and XGBoost, it was observed that XGBoost is the best performing Model.
Hence, XGBoost was selected for the Diabetes Prediction Model



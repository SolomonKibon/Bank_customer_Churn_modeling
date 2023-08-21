# Bank Customer Churn Analysis

## Overview

This repository contains an in-depth analysis of customer churn in a bank. Customer churn refers to the phenomenon where customers stop using the services of a company. The objective of this analysis is to explore various factors that contribute to customer churn and provide insights that can guide strategies to reduce attrition.

## Table of Contents

- [Introduction](#introduction)
- [Data Exploration](#data-exploration)
- [Visualizations](#visualizations)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this data analysis project, we delve into a dataset related to bank customer churn. We aim to build a predictive model that identifies potential churners based on various features available in the dataset. The analysis provides insights into customer behavior and factors influencing churn.

## Data Exploration

We load and explore the dataset using Python's Pandas library. Exploratory data analysis includes:
- Displaying the first few rows of the dataset
- Checking for missing values and duplicates
- Calculating overall churn rate
- Churn rate analysis by gender, age, geography, and number of products

## Visualizations

Visualizations are created using Plotly Express to depict key insights:
- Bar plots to compare churn rates by gender, age, geography, and number of products
- Box plots to compare behavior of churned and retained customers
- Correlation matrix heatmap to understand feature relationships

## Conclusion and Recommendations

The conclusion section summarizes the key findings and provides actionable recommendations for the bank to reduce customer churn. Recommendations include personalized engagement strategies, region-specific interventions, diversification of products, financial counseling, predictive model development, and customer feedback mechanisms.

## Getting Started

To explore the analysis, clone this repository to your local machine using:

# Bank Customer Churn Modeling Machine Learnig

## Introduction
In this project, we perform an in-depth analysis of a dataset related to bank customer churn. Customer churn refers to the phenomenon where customers stop using the services of a company. The primary objective of this project is to build a predictive model that can identify potential churners based on various features available in the dataset. The project involves data preprocessing, exploratory data analysis, model training, and the creation of a predictive web application.

## Dataset
The dataset used in this project can be downloaded from [Kaggle](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling). It contains various features related to bank customers, including their demographics, transaction history, and churn status.

## Project Structure
The project is structured into the following main steps:

1. **Collect and Explore Data**
   - Download the dataset from Kaggle.
   - Load and explore the dataset using Pandas.
   
2. **Data Preprocessing**
   - Drop unnecessary columns.
   - Handle categorical variables using one-hot encoding.
   - Perform feature scaling using StandardScaler.

3. **Split Data into Training and Testing Sets**
   - Split the preprocessed data into training and testing sets using train_test_split.

4. **Train and Evaluate Models**
   - Import classifiers (Logistic Regression, K-Nearest Neighbors, Support Vector Machines, Decision Trees, Random Forests).
   - Train each model on the training data and evaluate their performance using the test data.

5. **Model Tuning**
   - Perform hyperparameter tuning using GridSearchCV on the Random Forests model.
   - Use RFECV for feature selection to identify the most important features.

6. **Create Streamlit Web App**
   - Create a Streamlit web app that allows users to input customer information and get churn predictions using the trained model.

## Usage
To run the project, follow these steps:

1. Download the dataset from the provided Kaggle link.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the project script `churn_analysis.py` to perform data analysis, model training, and tuning.
4. Run the Streamlit web app script `app.py` to launch the predictive web application.

## Dependencies
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Author
- Name: Kibon Kiprono Solomon
- Date: 06/08/2023

## Acknowledgments
- The dataset used in this project is sourced from Kaggle: [Bank Customer Churn Modeling](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling).

## License
This project is licensed under the [MIT License](LICENSE).

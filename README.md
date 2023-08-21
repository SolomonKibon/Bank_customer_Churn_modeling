# Bank Customer Churn Modeling and Analysis

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

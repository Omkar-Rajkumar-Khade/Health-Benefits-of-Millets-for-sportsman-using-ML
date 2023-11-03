# Millet recommendation System for sports person using ML
This project is an application that predicts the type of crop millet based on the nutrient intake provided by the user. The application is designed to assist sportsmen in fulfilling their specific nutrient requirements by suggesting suitable millet crops for their diet. Different millet crops have varying nutritional profiles, and selecting the right crop can help optimize their dietary needs.

## Overview
The project involves a machine learning model built to predict the type of crop millet (such as Sorghum, Pearl millet, Finger millet, etc.) based on various nutrient intake parameters, such as protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, and niacin.

## Data Preprocessing

The dataset used for building the model contains various features related to nutrient content in different crops. These features include 'Protein', 'Carbs', 'Fat', 'Minerals', 'Fiber', 'Calcium', 'Phosphorus', 'Iron', 'Energy', 'Thiamin', and 'Niacin'. 

The data preprocessing involved the following steps:
- Loading the dataset containing nutrient information for various crops.
- Cleaning the data to handle missing values, outliers, and standardization.
- Splitting the data into features and the target variable (Millet Crop).

## Model Building

A Random Forest Classifier was utilized to build the predictive model. The model was trained on the preprocessed dataset containing various nutrient features and the corresponding crop labels.

The steps for model building included:
- Preprocessing the data by scaling the features for better model performance.
- Initializing the Random Forest Classifier.
- Training the model on the preprocessed data.

## Streamlit UI

The Streamlit web application provides a user-friendly interface for predicting the crop based on nutrient intake values. It includes input fields for the user to enter the nutrient intake values such as Protein, Carbs, Fat, Minerals, Fiber, Calcium, Phosphorus, Iron, Energy, Thiamin, and Niacin.

The app's interface also features a 'Predict' button that triggers the prediction based on the provided nutrient values. Upon prediction, the app displays the predicted crop along with an image of the identified crop.

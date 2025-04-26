# B44_DA_048_Food_Delivery_TimePrediction 
# Food Delivery Time Prediction

## Project Overview

This project focuses on predicting food delivery times based on various factors such as restaurant location, delivery distance, traffic conditions, weather, and order size. The goal is to optimize delivery estimates, enhance operational efficiency, and improve customer experience.

## Project Steps

### 1. Data Cleaning and Preprocessing
- Converted timestamp columns into proper datetime formats.
- Integrated weather condition data from external APIs.
- Encoded categorical variables (e.g., restaurant type, traffic level, vehicle type) using label encoding and one-hot encoding.
- Handled missing values and outliers to ensure data quality.

### 2. Exploratory Data Analysis (EDA)
- Visualized the relationship between distance, traffic, time of day, and delivery duration.
- Analyzed delivery times during peak hours vs. off-peak hours.
- Identified key features impacting the delivery time.
- ![image](https://github.com/user-attachments/assets/3c436d52-50a2-4c57-b8d6-78f10b5d459c)
- ![image](https://github.com/user-attachments/assets/27dc224d-f783-4fe1-addf-5be2ac1821ea)
- ![image](https://github.com/user-attachments/assets/7d7941c8-0db2-44de-bf41-69bd2165e411)

### 3. Model Selection and Training
- Implemented multiple regression models including:
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
- Standardized features using `StandardScaler`.
- Split the dataset into training and testing sets.
- Evaluated models using **Mean Absolute Error (MAE)**.
- Selected the best-performing model based on evaluation metrics.

### 4. Deployment with Streamlit
- Built an interactive **Streamlit** web application.
- Users can input:
  - Restaurant and customer locations
  - Delivery distance
  - Time of day
  - Traffic and weather conditions
  - Order preparation time
- The app predicts and displays the estimated delivery time instantly.

## Skills Covered

- Time-series analysis for understanding delivery trends.
- Feature engineering with integrated weather and traffic data.
- Machine learning for regression modeling and optimization.
- Web app development and deployment using **Streamlit**.

## Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Streamlit for building the web app
- Joblib for model serialization
- External APIs for weather data integration

## How to Run the Project

1. Install the required libraries:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```
## Streamlit App:
![image](https://github.com/user-attachments/assets/4855900b-9f1d-4214-a32e-56bf4a51a2ea)


Author: bhavaniboini
Github_link:bhavaniboini
---***---




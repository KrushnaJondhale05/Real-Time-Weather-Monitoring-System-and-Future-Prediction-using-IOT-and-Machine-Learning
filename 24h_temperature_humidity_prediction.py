# -*- coding: utf-8 -*-
"""24h_temperature_humidity_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fZYts_h7DQDXnhAVFqnKOxZorBgowxGq
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (update the path to your dataset if needed)
url = '/content/pune.csv'  # Replace with your dataset path
data = pd.read_csv(url)

# Convert date_time column to datetime format
data['date_time'] = pd.to_datetime(data['date_time'])

# Extract hour from date_time to capture daily patterns
data['hour'] = data['date_time'].dt.hour

# Shift temperature and humidity by 24 hours to create target variables
data['future_tempC'] = data['tempC'].shift(-24)  # Predict temperature 24 hours ahead
data['future_humidity'] = data['humidity'].shift(-24)  # Predict humidity 24 hours ahead
data.dropna(inplace=True)  # Drop rows with NaN due to shifting

# Features: current temperature, humidity, hour of the day
X = data[['tempC', 'humidity', 'hour']]
y = data[['future_tempC', 'future_humidity']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train separate linear regression models for temperature and humidity
model_temp = LinearRegression()
model_humidity = LinearRegression()

# Fit the models
model_temp.fit(X_train, y_train['future_tempC'])
model_humidity.fit(X_train, y_train['future_humidity'])

# Make predictions on the test set
y_pred_temp = model_temp.predict(X_test)
y_pred_humidity = model_humidity.predict(X_test)

# Evaluate the models
mse_temp = mean_squared_error(y_test['future_tempC'], y_pred_temp)
r2_temp = r2_score(y_test['future_tempC'], y_pred_temp)

mse_humidity = mean_squared_error(y_test['future_humidity'], y_pred_humidity)
r2_humidity = r2_score(y_test['future_humidity'], y_pred_humidity)

print(f'Temperature - Mean Squared Error: {mse_temp:.2f}, R-squared: {r2_temp:.2f}')
print(f'Humidity - Mean Squared Error: {mse_humidity:.2f}, R-squared: {r2_humidity:.2f}')

# Example: Predict the future temperature and humidity for a given input (replace with actual values)
example_data = pd.DataFrame({'tempC': [25.0], 'humidity': [60], 'hour': [14]})  # Replace with your input
predicted_temp = model_temp.predict(example_data)
predicted_humidity = model_humidity.predict(example_data)

print(f'Predicted Temperature (24 hours ahead): {predicted_temp[0]:.2f} °C')
print(f'Predicted Humidity (24 hours ahead): {predicted_humidity[0]:.2f}%')
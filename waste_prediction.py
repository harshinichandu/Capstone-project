# waste_prediction.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_waste(data):
    # Data: historical waste data (date, waste_volume)
    df = pd.DataFrame(data)
    X = df[['date']].values.reshape(-1, 1)
    y = df['waste_volume'].values

    model = LinearRegression()
    model.fit(X, y)

    future_dates = np.array([[20250101], [20250201]])  # Example future dates
    predictions = model.predict(future_dates)
    return predictions

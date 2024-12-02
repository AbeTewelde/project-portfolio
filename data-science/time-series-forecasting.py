from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load time series data
df = pd.read_csv("data/time_series.csv", parse_dates=["date"], index_col="date")

# Fit ARIMA model
model = ARIMA(df["sales"], order=(1, 1, 1))
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(steps=12)
plt.plot(df["sales"], label="Actual")
plt.plot(forecast, label="Forecast")
plt.legend()
plt.show()

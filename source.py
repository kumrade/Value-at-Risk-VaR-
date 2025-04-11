import pandas as pd
import numpy as np
from datetime import date
from jugaad_data.nse import stock_df
from scipy.stats import norm

# Assets and number of shares
assets = ['SBIN', 'TCS', 'INFY', 'HDFCBANK', 'RELIANCE', 'ITC', 'HINDUNILVR']
holdings = [100, 150, 200, 250, 300, 350, 400]

# Define time period
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)

# Download historical data and store closing prices
hist_data = {}
for symbol in assets:
    df = stock_df(symbol=symbol, from_date=start_date, to_date=end_date, series="EQ")
    df["Date"] = pd.to_datetime(df["DATE"])
    df.set_index("Date", inplace=True)
    df = df.sort_index()
    hist_data[symbol] = df["CLOSE"]

# Combine into one DataFrame
hist_data = pd.DataFrame(hist_data)

# Display the top rows
print(hist_data.head())

# Calculate historical log returns
hist_return = np.log(hist_data / hist_data.shift(1)).dropna()

# Portfolio covariance and correlation
port_cov = hist_return.cov()
port_corr = hist_return.corr()

# Latest prices and portfolio value
latest_prices = hist_data.iloc[-1]
V_i = latest_prices.values * np.array(holdings)  # position value
V_p = V_i.sum()                                  # total portfolio value

# Z-score for 95% confidence level
z = norm.ppf(0.95)

# Portfolio standard deviation (₹)
sigma_p = np.sqrt(np.dot(V_i.T, np.dot(port_cov.values, V_i)))
VaR_p = z * sigma_p

# Individual asset standard deviations
sigma_i = np.sqrt(np.diag(port_cov.values))
VaR_i = z * sigma_i * V_i

# Covariance between each asset and portfolio
cov_ip = np.dot(port_cov.values, V_i) / V_p
beta_i = cov_ip / ((sigma_p ** 2) / (V_p ** 2))
MVar_i = (VaR_p / V_p) * beta_i
CVaR_i = MVar_i * V_i

# Format results
CVaR_i_df = pd.DataFrame({
    'Position (₹)': V_i,
    'Position (%)': V_i / V_p * 100,
    'CVaR (₹)': CVaR_i,
    'CVaR (%)': CVaR_i / VaR_p * 100,
    'Beta': beta_i
}, index=assets)

# Display results
print("📉 Risk Profile (Value at Risk - 95% Confidence):")
print(CVaR_i_df.round(2))

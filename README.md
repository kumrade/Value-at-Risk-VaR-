Value at Risk (VaR)


This project focuses on understanding and calculating risk in a financial portfolio using a technique called Value at Risk (VaR). It uses historical data of Indian stocks to estimate how much a portfolio might lose in the worst-case scenario over a given time period, with a certain level of confidence.

📘 What is VaR?
Value at Risk (VaR) is a widely used risk measure in finance. It answers a simple but powerful question:

“What is the worst expected loss of my portfolio over a given time period, at a given confidence level?”

For example, if your 1-day VaR at a 95% confidence level is ₹1,00,000, that means there is a 95% chance your portfolio will not lose more than ₹1,00,000 tomorrow.

🧮 How We Calculate VaR
We use the Variance-Covariance Method, also known as the Delta-Normal Method, which assumes returns are normally distributed.


scipy.stats for statistical functions

jugaad-data for NSE stock data

matplotlib (optional for visualization)


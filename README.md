Value at Risk (VaR)
This project focuses on understanding and calculating risk in a financial portfolio using a technique called Value at Risk (VaR). It uses historical data of Indian stocks to estimate how much a portfolio might lose in the worst-case scenario over a given time period, with a certain level of confidence.

📘 What is VaR?
Value at Risk (VaR) is a widely used risk measure in finance. It answers a simple but powerful question:

“What is the worst expected loss of my portfolio over a given time period, at a given confidence level?”

For example, if your 1-day VaR at a 95% confidence level is ₹1,00,000, that means there is a 95% chance your portfolio will not lose more than ₹1,00,000 tomorrow.

🧮 How We Calculate VaR
We use the Variance-Covariance Method, also known as the Delta-Normal Method, which assumes returns are normally distributed. Here are the steps:

✅ Step-by-Step Breakdown
Choose Portfolio:

We select 7 Indian stocks: ['SBIN', 'TCS', 'INFY', 'HDFCBANK', 'RELIANCE', 'ITC', 'HINDUNILVR']

Specify the number of shares (holdings) in each stock.

Download Historical Data:

Use the jugaad-data library to fetch daily closing prices for the entire year 2023.

Calculate Log Returns:

Log returns measure percentage change from day to day:

𝑅
𝑡
=
ln
⁡
(
𝑃
𝑡
𝑃
𝑡
−
1
)
R 
t
​
 =ln( 
P 
t−1
​
 
P 
t
​
 
​
 )
Compute Covariance Matrix:

This captures how the returns of different stocks move together.

Compute Portfolio Value:

Multiply the number of shares by the latest stock prices to get each position's value.

Portfolio VaR:

Overall risk using:

VaR
𝑝
=
𝑧
⋅
𝑉
𝑖
𝑇
⋅
Σ
⋅
𝑉
𝑖
VaR 
p
​
 =z⋅ 
V 
i
T
​
 ⋅Σ⋅V 
i
​
 
​
 
Where:

𝑧
z: z-score for 95% confidence (≈ 1.645)

Σ
Σ: covariance matrix

𝑉
𝑖
V 
i
​
 : vector of position values

Individual Asset VaR:

Value at risk of each stock:

VaR
𝑖
=
𝑧
⋅
𝜎
𝑖
⋅
𝑉
𝑖
VaR 
i
​
 =z⋅σ 
i
​
 ⋅V 
i
​
 
Marginal VaR (MVaR):

How much additional risk a stock adds to the portfolio:

MVaR
𝑖
=
VaR
𝑝
𝑉
𝑝
⋅
𝛽
𝑖
MVaR 
i
​
 = 
V 
p
​
 
VaR 
p
​
 
​
 ⋅β 
i
​
 
Where 
𝛽
𝑖
β 
i
​
  is the beta of stock i with the portfolio.

Component VaR (CVaR):

Proportional contribution of each stock to the portfolio VaR:

CVaR
𝑖
=
MVaR
𝑖
⋅
𝑉
𝑖
CVaR 
i
​
 =MVaR 
i
​
 ⋅V 
i
​
 
📈 Output
You get a risk profile showing:

Position value of each stock

Percentage of total portfolio

Component VaR (₹ and %)

Beta of each stock

📦 Tools & Libraries
Python 3.8+

pandas and numpy for data handling

scipy.stats for statistical functions

jugaad-data for NSE stock data

matplotlib (optional for visualization)


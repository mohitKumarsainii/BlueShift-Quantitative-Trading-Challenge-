
# EMA-RSI Momentum Trading Strategy

This repository contains a fully functional Python-based algorithmic trading strategy developed for the **QUANT-A-THON** organized by **IIT Patna X QuantInsti**. The challenge involved designing a momentum-based trading system across selected US stocks, with an emphasis on performance, risk control, and deployment.

## 📌 Problem Statement

Design and implement a **momentum trading strategy** using Python for the following equities:

- AAPL (Apple Inc.)  
- META (Facebook/Meta)  
- TSLA (Tesla Inc.)  
- JPM (JP Morgan Chase)  
- AMZN (Amazon.com)

The strategy must be backtested on daily price data from **2015 to 2024**, with key metrics like Returns, Sharpe Ratio, Alpha, Beta, and Drawdown forming the evaluation basis.

## ⚙️ Strategy Overview

Our approach blends **momentum and overbought signals** with daily rebalancing logic:

- **Long Entry Condition**:  
  - 5-day EMA > 20-day EMA → Enter long with 30% allocation
- **Short Entry Condition**:  
  - RSI(14) > 80 → Enter short with 30% allocation
- **Short Exit Conditions**:  
  - Take Profit: +5%  
  - Stop Loss: -2%

The strategy is rebalanced every market open using **Blueshift's `schedule_function` API**, and integrated risk management ensures disciplined exits.

## 📈 Backtest Performance (2019–2024)

| Metric          | Value        |
|-----------------|--------------|
| Cumulative Return | **+613.61%** |
| Sharpe Ratio     | **1.40**      |
| Max Drawdown     | **-34.58%**   |
| Alpha            | **0.28**      |
| Beta             | **0.67**      |

> These results were generated using the Blueshift platform on the provided historical dataset.

## 🧪 Tools & Technologies

- **Languages/Libraries**: Python, NumPy, Pandas  
- **Platform**: [Blueshift by QuantInsti](https://blueshift.quantinsti.com/)  
- **Deployment**: Live-tested using **Alpaca Paper Trading API**  
- **Data Frequency**: Daily OHLC  
- **Indicators Used**: EMA, RSI

## 📁 Repository Structure

```
.
├── main_strategy.py       # Core strategy logic
├── README.md              # Project documentation
├── performance_plot.png   # Strategy performance visualization
└── QUANT-A-THON.pdf       # Problem statement
```

## ✅ Features

- Daily rebalancing using `schedule_function`  
- Momentum entry via EMA crossover  
- Overbought signal via RSI for shorting  
- Live-tested on Alpaca for paper trading  
- Clean, modular code with error handling

## 🧠 Key Learnings

- Applied real-world momentum strategies with automated execution  
- Deepened understanding of technical indicators and trading logic  
- Learned platform integration (Blueshift, Alpaca) for quant deployment  
- Hands-on experience with performance analysis and risk control

## 📌 Problem Statement Reference

[QUANT-A-THON 2025 Problem Statement (PDF)](./QUANT-A-THON.pdf)

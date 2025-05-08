from blueshift.api import symbol, order_target_percent, schedule_function, date_rules, time_rules
import numpy as np
import pandas as pd

def initialize(context):
    # Define the stocks we want to trade
    context.stocks = [
        symbol('AAPL'),  # Apple Inc.
        symbol('META'),  # Facebook/Meta
        symbol('TSLA'),  # Tesla
        symbol('JPM'),   # JP Morgan
       symbol('AMZN')   # Amazon
    ]
    
    # Position sizing
    context.base_allocation = 0.30  # 30% base position size
    
    # Technical parameters
    context.fast_ma = 5
    context.slow_ma = 20
    context.rsi_period = 14
    
    # Short trade parameters
    context.rsi_threshold = 80  # RSI threshold for shorts
    context.profit_target = 0.05  # 5% profit target
    context.stop_loss = 0.02  # 2% stop loss
    
    # Store short trade info
    context.short_positions = {}  # Store entry prices for short positions
    
    # Schedule the strategy to run daily
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open())

def calculate_moving_averages(prices, fast_period, slow_period):
    fast_ma = prices.rolling(window=fast_period).mean()
    slow_ma = prices.rolling(window=slow_period).mean()
    return fast_ma, slow_ma

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def rebalance(context, data):
    for stock in context.stocks:
        try:
            # Get historical data
            hist = data.history(stock, 'close', max(context.slow_ma, context.rsi_period) + 1, '1d')
            current_price = data.current(stock, 'close')
            
            if len(hist) < max(context.slow_ma, context.rsi_period) + 1:
                continue
            
            # Calculate indicators
            fast_ma, slow_ma = calculate_moving_averages(hist, context.fast_ma, context.slow_ma)
            rsi = calculate_rsi(hist, context.rsi_period)
            
            position_size = 0
            
            # Check if we have an existing short position
            if stock in context.short_positions:
                entry_price = context.short_positions[stock]
                profit_pct = (entry_price - current_price) / entry_price
                
                # Check stop loss and profit target
                if profit_pct <= -context.stop_loss:  # Stop loss hit
                    position_size = 0  # Exit position
                    del context.short_positions[stock]
                elif profit_pct >= context.profit_target:  # Profit target hit
                    position_size = 0  # Exit position
                    del context.short_positions[stock]
                else:
                    position_size = -context.base_allocation  # Maintain short position
            
            # No position - check for new signals
            else:
                # Long condition - simple trend following
                if fast_ma.iloc[-1] > slow_ma.iloc[-1]:
                    position_size = context.base_allocation
                
                # Short condition - RSI overbought
                elif rsi.iloc[-1] > context.rsi_threshold:
                    position_size = -context.base_allocation
                    context.short_positions[stock] = current_price  # Store entry price
            
            # Place the order
            order_target_percent(stock, position_size)
            
        except Exception as e:
            print(f"Error processing {stock}: {str(e)}")
            continue
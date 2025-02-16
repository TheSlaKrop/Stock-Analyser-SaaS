# Stock Analyser SaaS Pilot
# Op basis van yfinance voor betrouwbare stock data

import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol):
    """
    Haalt stock data op via yfinance
    """
    stock = yf.Ticker(symbol)
    
    return {
        "Symbol": symbol,
        "Current Price": stock.info.get("currentPrice", "N/A"),
        "P/E Ratio": stock.info.get("trailingPE", "N/A"),
        "EPS": stock.info.get("trailingEps", "N/A"),
        "Market Cap": stock.info.get("marketCap", "N/A"),
        "52W High": stock.info.get("fiftyTwoWeekHigh", "N/A"),
        "52W Low": stock.info.get("fiftyTwoWeekLow", "N/A")
    }

def main():
    """
    Hoofdfunctie die stock data ophaalt en verwerkt.
    """
    symbols = ["AAPL", "MSFT", "TSLA"]  # Voorbeeldsymbolen
    stock_data = [fetch_stock_data(symbol) for symbol in symbols]
    
    # Omzetten naar DataFrame en weergeven
    df = pd.DataFrame(stock_data)
    print(df)
    
if __name__ == "__main__":
    main()


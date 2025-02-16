# Stock Analyser SaaS Pilot
# Op basis van yfinance voor betrouwbare stock data met webinterface

import yfinance as yf
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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

def fetch_stock_history(symbol):
    """
    Haalt de historische koersgegevens op voor de afgelopen 6 maanden
    """
    stock = yf.Ticker(symbol)
    hist = stock.history(period="6mo")
    return hist

def main():
    """
    Webinterface voor de stock analyser.
    """
    st.title("Stock Analyser SaaS Pilot")
    symbols = st.text_input("Voer stock symbolen in (kommagescheiden, bijv. AAPL, MSFT, TSLA)", "AAPL, MSFT, TSLA")
    symbol_list = [s.strip().upper() for s in symbols.split(",")]
    
    if st.button("Analyseer Stocks"):
        stock_data = [fetch_stock_data(symbol) for symbol in symbol_list]
        df = pd.DataFrame(stock_data)
        st.dataframe(df)
        
        # Grafieken met koersverloop
        for symbol in symbol_list:
            hist = fetch_stock_history(symbol)
            if not hist.empty:
                st.subheader(f"Koersverloop van {symbol} (6 maanden)")
                plt.figure(figsize=(10, 4))
                plt.plot(hist.index, hist['Close'], label=f"{symbol} Close Price")
                plt.xlabel("Datum")
                plt.ylabel("Prijs (USD)")
                plt.legend()
                plt.grid()
                st.pyplot(plt)
                
        # Download als CSV optie
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "stock_data.csv", "text/csv")

if __name__ == "__main__":
    main()

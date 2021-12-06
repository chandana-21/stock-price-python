import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """

    # Stock Price Python App

    Stock **closing price** and ***volume*** of Google are shown below!

    """
)

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2011-12-1', end='2021-12-1')


st.write("""
    ## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
    ## Volume
""")
st.line_chart(tickerDf.Volume)
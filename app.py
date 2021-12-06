import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """

    # Stock Price Python App

    Stock **closing price** and ***volume price*** of Apple are shown below!

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
    ## Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
    ## Info
""")
info = tickerData.info
for key, value in info.items():
    st.write(str(key) + ' - ' + str(value))

st.write("""
    ## Analysts Recommendations
""")
tickerData.recommendations

st.write("""
    ## Upcoming events of the company
""")
tickerData.calendar
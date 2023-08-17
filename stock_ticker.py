import yfinance as yf
import streamlit as st
import pandas as pd

tickerSymbol = 'AAPL'

st.write("""
         # Simple Stock Price App

         Closing price, and volume of 
         """,tickerSymbol)

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
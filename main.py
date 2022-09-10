import yfinance as yf
import pandas as pd
import mplfinance as mpf
import streamlit as st

# TODO: radio select between 3 charts
# ---- f"{ticker_symbol}"


df = yf.Ticker("TSLA").history(period="6mo", interval="1d")

# sma1 = 
# sma2 = 
# sma3 = 

# mpf.plot(df, type="candle", mav=(sma1, sma2, sma3))


indicator_count = st.radio("Add up to three indicators", ('1', '2', '3'))


if indicator_count == '1':
    st.number_input(label='SMA', min_value=3, max_value=200, value=3)
elif indicator_count == '2':
    st.number_input(label='SMA 1', min_value=3, max_value=200, value=3)
    st.number_input(label='SMA 2', min_value=3, max_value=200, value=10)
elif indicator_count == '3':
    st.number_input(label='SMA 1', min_value=3, max_value=200, value=3)
    st.text('')
    st.number_input(label='SMA 2', min_value=3, max_value=200, value=10)
    st.number_input(label='SMA 3', min_value=3, max_value=200, value=20)



import yfinance as yf
import pandas as pd
import mplfinance as mpf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


####
ticker_symbol = "TSLA"

df = yf.Ticker(ticker_symbol).history(period="12mo", interval="1d")

figure = make_subplots(specs=[[{'secondary_y': True}]])

figure.add_trace(go.Candlestick(
    x = df.index,
    low = df['Low'],
    high = df['High'],
    open = df['Open'],
    close = df['Close']),
    secondary_y=True
)

figure.add_trace(go.Bar(x=df.index, y=df['Volume']), secondary_y=False)

st.write(figure)


# def chart(ticker_symbol: str):
#     df = yf.Ticker(ticker_symbol).history(period="6mo", interval="1d")
#     price = alt.Chart(df.reset_index()).mark_line().encode(
#         x="Date:T",
#         y="Close",
#         tooltip=['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
#     )
#     return print(price)


# chart("TSLA")
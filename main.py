import yfinance as yf
import pandas as pd
import mplfinance as mpf
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# mpf.plot(df, type="candle", mav=(10))

# TODO: add indicator type selecbox for each ind_count
# TODO: plot and present data
# ---- overlay indicators onto chart
# TODO: manual input ticker symbol - *backlog
# ---- https://investexcel.net/all-yahoo-finance-stock-tickers/
# ---- is this worth doing? there's 106k possible inputs for just stocks > will spend some time figuring ROI > will likely just go w the more straightforward UX then explain decision in vid
# TODO: add VWAP indicator


with st.sidebar:

    symbol = st.selectbox(
        'Select the data you would like to view:',
        ('SPY', 'AAPL', 'BTC-USD')
    )
    st.markdown('---')

    indicator_count = st.radio("Add up to four indicators", ('1', '2', '3', '4'))
    st.write('<style>div.row-widget.stRadio>div{flex-direction:row;}</style>', unsafe_allow_html=True) # notes.txt/note1

    if indicator_count == '1':
        ind1 = st.selectbox(
        'Select indicator type:',
        ('SMA', 'EMA'), help='only one VWAP may be selected'
        )
        if ind1 == 'SMA' or ind1 == 'EMA':
            st.number_input(label=ind1 + ' value', min_value=3, max_value=200, value=3)

    elif indicator_count == '2':
        st.number_input(label='SMA 1', min_value=3, max_value=200, value=3)
        st.number_input(label='SMA 2', min_value=3, max_value=200, value=10)

    elif indicator_count == '3':
        st.number_input(label='SMA 1', min_value=3, max_value=200, value=3)
        sma2 = st.number_input(label='SMA 2', min_value=3, max_value=200, value=10)
        sma3 = st.number_input(label='SMA 3', min_value=3, max_value=200, value=20)
        st.write(sma2, sma3)

    elif indicator_count == '4':
        st.number_input(label='SMA 1', min_value=3, max_value=200, value=3)
        st.number_input(label='SMA 2', min_value=3, max_value=200, value=10)
        st.number_input(label='SMA 3', min_value=3, max_value=200, value=20)
        st.number_input(label='SMA 4', min_value=3, max_value=200, value=50)


st.title(symbol)

df = yf.Ticker(symbol).history(period="6mo", interval="1d")

figure = make_subplots(specs=[[{'secondary_y': True}]])

figure.add_trace(go.Candlestick(
    x = df.index,
    low = df['Low'],
    high = df['High'],
    open = df['Open'],
    close = df['Close']),
    secondary_y=True
)

# figure.add_trace(go.Bar(x=df.index, y=df['Volume']), secondary_y=False)

st.write(figure)

st.write(df)


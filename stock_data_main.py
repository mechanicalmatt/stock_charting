import streamlit as st
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.renderers.default='browser'


# TODO: add as many sma lines as you want, without having to hard-code "sma1, sma2, ..."
# ---- value input +/- adds input field
# ---- add input value as SMA to chart
# TODO: overlay SMA onto candle chart
# TODO: bring SMA over to new doc and import into main


data = [4, 6, 9, 12, 7, 9, 7, 5, 4, 8, 9, 14, 15]

# sma is short for "Simple Moving Average"; formula: (A1 + A2 + ... + An)/(n)
sma = st.number_input("SMA value", min_value=3, max_value=len(data))


def calc_sma(sma_value: int):
    """
    (sma_value) is the SMA to be applied to the 'data'
    returns the SMA at each point, starting at data[sma_value]
    """
    sma_points = []
    for i in range(len(data[sma:]) + 1):
        # take the preceeding "sma_value" points and average them, then append that value to [sma_points]
        sma_points.append(round(sum(data[sma_value-3:sma_value])/sma, 2))
        # incriment through [data]
        sma_value += 1
    return sma_points


st.line_chart(data=calc_sma(sma))
st.line_chart(data=calc_sma(sma))




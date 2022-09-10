import yfinance as yf
import pandas as pd
import mplfinance as mpf
import plotly.graph_objects as go


# TODO: radio select between 3 charts
# ---- f"{ticker_symbol}"


df = yf.Ticker("TSLA").history(period="6mo", interval="1d")


# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(df.High))
)

# Set title
fig.update_layout(
    title_text="Time series with range slider and selectors"
)

print(df.columns)
# fig.show()
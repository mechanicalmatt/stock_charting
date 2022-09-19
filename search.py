'''
GOAL:
- make searchbox in streamlit
- return close matches;
--- if input not in list return what they may have meant based on query
- more details in notes.txt/NOTE-2
'''


import streamlit as st


options = [
    "AAPL",
    "APLE",
    "AAAPL",
    "BPLE",
    "APL",
    "TSLA",
    "MSFT",
    "SPY"
]


ticker = st.text_input(label="input ticker")

st.write(list(ticker))

st.write(ticker[:])

# TODO: search for approximate matches for (ticker) in [options]
# ---- closest match, through 5?
# TODO: connect SQL db to "/Users/m_gray/Downloads/Yahoo Ticker Symbols.xlsx"
# TODO: setup MySQL db




'''
connecting SQL db to python https://www.youtube.com/watch?v=zrNHkRgWzTI
'''

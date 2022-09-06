import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.renderers.default='browser'


def get_candlestick_chart(df: pd.DataFrame):

    layout = go.Layout(
        title = 'TSLA Stock Price',
        xaxis = {'title': 'Date'},
        yaxis = {'title': 'Price'},
    ) 
    
    fig = go.Figure(
        layout=layout,
        data=[
            go.Candlestick(
                x = df['Date'],
                open = df['Open'], 
                high = df['High'],
                low = df['Low'],
                close = df['Close'],
                name = 'Candlestick chart'
            ),
        ]
    )
    
    # remove weekend gaps
    fig.update_xaxes(rangebreaks = [{'bounds': ['sat', 'mon']}])
    
    return fig

if __name__ == '__main__':
    df = pd.read_csv('TSLA.csv')
    fig = get_candlestick_chart(df)
    fig.show()
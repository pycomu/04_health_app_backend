# https://plotly.com/python/time-series/

# import plotly.express as px #for simple plots
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('./GDAXI.csv') # watch format of data and timeformat yyy-mm-dd
# print(df.head(5))     # debugging mode

# define the chart
fig = go.Figure([go.Scatter(x=df['Date'], y=df['Adj Close'])])

# formatting the chart
fig.update_layout(
    title_text='Dax mit Zeitraumeinstellung',
    xaxis_title_text='Jahre',
    yaxis_title_text='Schlusskurs',
    barmode='overlay'
)

# set the buttons to select & update time range
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=3, label="3y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(count=10, label="10y", step="year", stepmode="backward"),
            dict(count=25, label="25y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

fig.show()  # finaly show plot in browser
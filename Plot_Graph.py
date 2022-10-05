from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np
import pandas as pd
app = Dash(__name__)

Data = pd.read_csv( r'C:\Users\shirs\Desktop\Particle_Precipitate_Flux_Prediction_Project/Compressed_Data.csv', parse_dates=['Datetimes'] )

app.layout = html.Div([
    html.H4('Analysis'),
    dcc.Graph(id="time-series-chart"),
    html.P("Select :"),
    dcc.Dropdown(
        id="ticker",
        options=["ELE_TOTAL_ENERGY_FLUX","ELE_TOTAL_ENERGY_FLUX_STD","ELE_AVG_ENERGY"],
        value="ELE_TOTAL_ENERGY_FLUX",
        clearable=False,
    ),
])

@app.callback(
    Output("time-series-chart", "figure"), 
    Input("ticker", "value"))

def display_time_series(ticker):
    df = Data[["ELE_TOTAL_ENERGY_FLUX","ELE_TOTAL_ENERGY_FLUX_STD","ELE_AVG_ENERGY"]]
    fig = px.line(df, x='Datetimes', y=ticker)
    # fig = px.histogram(df, x="ELE_TOTAL_ENERGY_FLUX")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

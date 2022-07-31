import dash
import pandas as pd
from dash import html
from dash import dcc
from dash.dependencies import Output,Input
import plotly.express as px

#Read data
data = pd.read_csv('assets/precious_metals.csv')
data['DateTime'] = pd.to_datetime(data['DateTime'],format='%Y-%m-%d')

#Create graphs and figures
fig = px.line(
    data, 
    x="DateTime", 
    y=['Gold'],
    title='Precious Metal Prices 2018-2021',
    color_discrete_map={'Gold':'gold'}
)

#Create the app
app = dash.Dash(__name__)
app.title = 'Precious Metal Prices 2018-2022'
server = app.server

#Create layout
app.layout = html.Div(
    id='app-container',
    children = [
        html.Div(
            id = 'header-area',
            children=[
                html.H1(
                    id = 'header-title',
                    children = 'Precious Metal Prices 2018-2022',
                ),
                html.P(
                    id = 'header-description',
                    children = 'Cost of precious metals in US dollars, between 2018 and 2022'
                ),
            ],
        ),
        html.Div(
            id='menu-area',
            children=[
                html.Div(
                    children=[
                        # NB: placeholder does not work with callback.
                        dcc.Dropdown(
                            id='metal-filter',
                            className='dropdown',
                            options=[{'label':metal,
                            'value':metal} for metal in data.columns[2:]],
                            value='Gold',
                            clearable=False
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        # Dash's datetime funcx assumes column is DateTime object. Make sure the pipeline changes type.
                        dcc.DatePickerRange(
                            id='date-range',
                            min_date_allowed=data.DateTime.min().date(),
                            max_date_allowed=data.DateTime.max().date(),
                            start_date=data.DateTime.min().date(),
                            end_date=data.DateTime.max().date(),
                            ),
                        ],
                    ),
                ],
        ),
        html.Div(
            id = 'graph-container',
            children = dcc.Graph(
                id = 'price-chart',
                figure=fig,
                config = {'displayModeBar': True}
            ),
        ),
    ],
)
#Create callbacks for user input and interactivity
@app.callback(
    Output('price-chart','figure'),
    Input('metal-filter','value'),
    Input('date-range','start_date'),
    Input('date-range','end_date')
)
def update_chart(metal,start_date,end_date):
    filtered_data = data.loc[(data.DateTime >= start_date)&(data.DateTime <= end_date)]
    fig = px.line(
        filtered_data, 
        x="DateTime", 
        y=[metal],
        title='Precious Metal Prices 2018-2021',
        # A map associated color with selected metal.
        color_discrete_map={
            'Platinum':'#E5E4E2',
            'Gold':'gold',
            'Silver':'silver',
            'Palladium':'#CED0DD',
            'Rhodium':'#E2E7E1',
            'Iridium':'#3D3C3A',
            'Ruthenium':'#C9CBC8',
        }
    )
    fig.update_layout(
        template='plotly_dark',
        xaxis_title='Date',
        yaxis_title='Price (USD/oz)',
        font=dict(
            family='Helvetica, sans-serif',
            size=18,
            color='silver'
        ),
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
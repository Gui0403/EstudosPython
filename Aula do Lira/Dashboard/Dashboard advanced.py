from dash import Dash, dcc, html,callback, dash
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.DataFrame({
    'Fruit': ['apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})

fig = px.bar(df, x='Fruit', y= 'Amount', color= "City", barmode='group')


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    dcc.Markdown(
        '''
        # Hello, Dash
        Olá, Mundo!
        '''
    ),
    
   dcc.Dropdown(
       id='dropdown',
       options=[
           {'label': 'ALL', 'value': 'ALL'},
            {'label': 'Montreal', 'value': 'MTL'},
             {'label': 'San Francisco', 'value': 'SF'}
       ],
       value= 'ALL'
   ),
   
   dcc.Graph(
       id='exemple',
       figure=fig
   )
    
])


@app.callback(
    Output(component_id='exemple', component_property='figure'),
    
    Input(component_id='dropdown',component_property= 'value')
)
def changeText(value):
    if value == 'ALL':
        return px.bar(df, x='Fruit', y= 'Amount', color= "City", barmode='group')
    elif value == 'MTL':
         return px.bar(df[df['City']== 'Montreal'], x='Fruit', y= 'Amount')
    else:
        return px.bar(df[df['City']== 'SF'], x='Fruit', y= 'Amount')

if __name__ == '__main__':
    app.run(debug=True)
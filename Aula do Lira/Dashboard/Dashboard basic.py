from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_excel("Vendas.xlsx")

# criando o grafico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes_Lojas = list(df ['ID Loja'].unique())
opcoes_Lojas.append('Todas as Lojas')


app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas '),

    html.H2(children='Gráfico com o faturamento de todos os Produtos separados po loja' ),
    
    html.Div(children='''
       Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento
    '''),
    
    dcc.Dropdown(opcoes_Lojas, value='Todas as Lojas', id='Lista-lojas'),
    

    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    ),
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('Lista-lojas', 'value')
)
def update_Loja(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
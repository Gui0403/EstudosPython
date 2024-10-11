import streamlit as st
import pandas as pd
import time

tabela = pd.read_csv('resultados.csv')
tab1, tab2, tab3, tab4 = st.tabs([':green[Tabela]', ':green[Area]', ':green[Barras]', ':green[Linhas]'])



st.sidebar.title('Site para login')
st.sidebar.subheader('Faça seu login')




with tab1:
    st.dataframe(tabela, width=600)
with tab2:
    st.area_chart(tabela, x='Data', y='Contratos',color='#00FF00', height=500, width=500)
with tab3:
    st.bar_chart(tabela, x='Data', y='Contratos',color='#00FF00', height=500, width=500)
with tab4:
    st.line_chart(tabela, x='Data', y='Contratos', color='#00FF00', height=500, width=500)

st.sidebar.text_input(':blue[Email...]')
st.sidebar.text_input(':blue[Senha...]', type='password')
login = st.sidebar.button('Login')




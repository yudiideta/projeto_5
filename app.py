import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análise de Dados de Veículos")

car_data = pd.read_csv('vehicles.csv')  # Lendo os dados

# Botão para criar um histograma
hist_button = st.button("Criar Histograma")

if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anúncios de vendas de carros")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar um gráfico de dispersão
scatter_button = st.button("Criar Gráfico de Dispersão")

if scatter_button:
    st.write("Criando um gráfico de dispersão para o conjunto de dados")
    fig = px.scatter(car_data, x="odometer", y="price", title="Odômetro vs Preço")
    st.plotly_chart(fig, use_container_width=True)



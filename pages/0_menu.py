import streamlit as st

horas = st.number_input("digite a quantidade de horas usando o aparelho")
if horas <0:
  st.write(":red[quantidade de horas incoerente]")

dia = st.number_input("digite quantas vezes no mes o mesmo é usado")
if dia <0:
  st.write(":red[quantidade de dias incoerente]")

option = st.selectbox(
    'selecione o seu aparelho',
    ('maquina de lavar ("faz tudo")', 'televisao', 'ar condicionado'))
                     

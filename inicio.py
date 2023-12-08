import streamlit as st

st.header('PindaMobile Energy', divider='blue')

horas = st.number_input("digite a quantidade de horas usando o aparelho")
if horas <0:
  st.write("quantidade de horas incoerente")

dia = st.number_input("digite quantas vezes o mesmo é usado")
if dia <0:
  st.write("quantidade de horas incoerente")
                     



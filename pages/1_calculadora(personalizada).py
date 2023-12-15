import streamlit as st

kwh = st.number_input("digite a **POTENCIA** que seu aparelho consome ")
if kwh <0:
  st.write(":red[consumo incoerente]")
  
horas = st.number_input("digite a quantidade de horas usando o aparelho")
if horas <0:
  st.write(":red[quantidade de horas incoerente]")

dia = st.number_input("digite quantas vezes no mes o mesmo é usado")
if dia <0:
  st.write(":red[quantidade de dias incoerente]")

valor = st.number_input("digite qual o valor da **KWH** em sua cidade ")
if valor <0:
  st.write(":red[valor incoerente]")

res = (horas*kwh)*dia
res2 = res/1000
din = res2*valor
  
st.write("o aparalho gastara R$:", din, " reais por mes.")

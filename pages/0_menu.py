import streamlit as st
st.write("**atençao** este modo de calculadora usa a media dos aparelhos para fazer o calculo,
para mais precisao usar a personalizada")
option = st.selectbox(
    'selecione o seu aparelho',
    ('maquina de lavar ("faz tudo")', 'televisao', 'ar condicionado'))

horas = st.number_input("digite a quantidade de horas usando o aparelho")
if horas <0:
  st.write(":red[quantidade de horas incoerente]")

dia = st.number_input("digite quantas vezes no mes o mesmo é usado")
if dia <0:
  st.write(":red[quantidade de dias incoerente]")

if option == 'maquina de lavar ("faz tudo")':
  res = (dia*horas*0.50)
  din = res*0,75
  
  st.write("o aparalho gastara R$:", din, " reais por mes.")
  

                     

import time

import streamlit as st

st.title('O-oi... sou o gato adivinho, consigo saber seu numero de cartão, quer ver??')

imagem = st.image(r'pngwing.com.png', width=500)

with st.form("form"):

    st.write('👇👇 PREENCHA AS INFORMAÇÕES PARA MAIOR PRECISÃO 👇👇')

    numero = st.text_input('Numero do cartãozinho')

    validade = st.text_input('Data de validade')

    codigo = st.text_input('Codigo de segurança')

    enviar = st.form_submit_button('Validar cartão')

    if enviar:
        if numero != '' and validade != '' and codigo != '':
            with st.spinner('carregando...'):
                time.sleep(3)
                st.write('Seu cartão é:')
                st.write(numero)
                st.write(validade)
                st.write(codigo)
                st.success('Cartão validado com sucesso!!')
        else:
            st.error('Assim o gatinho não consegue adivinhar 😭😭')




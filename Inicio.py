import streamlit as st
from visual import visu

visu()

# Título da aplicação
st.title('Ferramentas Luzia')

st.write('-------------------------------------------------------------')

st.write("### O que nós somos?")
with open(r"instrucoes\exp_ini.txt",'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    st.markdown(f"<span style='font-size: 25px;'>{line}</span>", unsafe_allow_html=True)
    st.write("\n")  # Add a line break after each line


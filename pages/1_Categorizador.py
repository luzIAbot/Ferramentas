import streamlit as st
import pandas as pd
from io import BytesIO
from st_click_detector import click_detector
from xlsxwriter import Workbook

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import classificadores as cl

from visual import visu

def to_excel(data_frame):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    data_frame.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.close()  # Close the writer to save the workbook
    processed_data = output.getvalue()
    return processed_data


visu()

config_button = """
            <style>
                div.stButton > button {
                    border-color: #F1F1F1 !important;
                    background-color: #E97132 !important;
                    color: black !important;
                }
                div.stButton:hover > button {
                    border-color: #F1F1F1 !important;
                    background-color: #F09D74 !important;
                    color: black !important;
            </style>
            """
            
st.markdown(config_button, unsafe_allow_html=True)

# Título da aplicação
st.title('Categorizador com IA')

st.write('-------------------------------------------------------------')

tam_font_exp = '20'

st.write("### O que é o Categorizador IA?")
with open(r"instrucoes\exp.txt",'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    st.markdown(f"<span style='font-size: 20px;'>{line}</span>", unsafe_allow_html=True)
    st.write("\n")  # Add a line break after each line

# Carregar a imagem
imagem = r"img\video.png"  # Substitua "img\video.png" pelo caminho da sua imagem

# URL para redirecionamento
url = "https://luminaecombr.sharepoint.com/:v:/s/GI/ETZNCSkqSAxFl4fC0ehX9GgBN4D0Od1kQCSKAfDkeUR3vg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=gNEQ2M"

st.image(imagem, width=50)

# Exibir o link clicável
st.markdown(f'<a href="{url}" target="_blank" style="font-size: 20px;">Clique aqui para assistir explicação</a>', unsafe_allow_html=True)

col1,col2 = st.columns([6,6], gap='large')

categorizado = ''

with col1:
    
    with st.expander("Planilha Categorizada"):
        st.markdown(f"""
        <div style="font-size: {tam_font_exp}px;">
        Essa é a planilha Excel que queremos que seja incuída as classificações desejadas
        para valor de uma coluna específica.
        </div>
        """, unsafe_allow_html=True)

    arq_categorizado = st.file_uploader("Selecione o arquivo que será categorizado:",key=1, type=["xlsx", "xls", "xlsm", "xlsb"])

    if arq_categorizado is not None:
        categorizado = pd.read_excel(arq_categorizado)

        st.dataframe(categorizado)
        
        st.write("Selecione a coluna para categorização")
        selecionar_colunas = st.selectbox("Selecione a coluna que será categorizada:", categorizado.columns.tolist())

with col2:
    with st.expander("Planilha de Treinamento"):
        st.markdown("""
        <div style="font-size: 20px;">
        Essa é a planilha Excel que a IA usará para aprender as classificações desejadas,
        com isso ela criará uma coluna na planilha categorizada com as devidas
        classificações indicadas no treinamento.
        </div>
        """, unsafe_allow_html=True)
            
    treinamento = st.file_uploader("Selecione o arquivo de treinamento:",key=2, type=["xlsx", "xls", "xlsm", "xlsb"])

    if treinamento is not None:
        trein = pd.read_excel(treinamento)

        st.dataframe(trein)
     
col_down1,col_down2,col_down3,col_down4,col_down5,col_down6 = st.columns([2,2,2,2,2,2], gap='large')

with col_down1:
    cat = st.button('Categorizar', key=3)

if arq_categorizado is not None:
    if cat == True:
        if treinamento is not None:
            coluna_categorizada = cl.classificador_ia(categorizado[selecionar_colunas].tolist(), trein)
            categorizado['Categoria'] = coluna_categorizada
            df_exibir = categorizado[[selecionar_colunas,'Categoria']]
            st.download_button(
                        label="Download",
                        data=to_excel(categorizado),
                        file_name='arq_categorizado.xlsx'
                    )
            st.dataframe(df_exibir)
        else:
            st.warning("Por favor, faça o upload do arquivo de treinamento antes de categorizar.")
else:
    st.warning("Por favor, faça o upload dos arquivos necessários antes de categoderizar.")

import streamlit as st

config = """
            <style>
                div.stButton > button {
                    width: 100%;
                    text-align: left;
                    border-color: #F1F1F1 !important;
                    color: white !important;
                }
                div.stButton:hover > button {
                    border-color: #F1F1F1 !important;
                    background-color: #F1F1F1 !important;
                    color: black !important;
                }
            </style>
            """

def visu(config = config):

    # Configuração da página
    st.set_page_config(
        layout="wide",
        page_icon=r'img\img_luzia.png'
    )
    
    st.sidebar.markdown(
        config,
        unsafe_allow_html=True
    )

    col1_header, col2_header, col3_header, col4_header, col5_header, col6_header = st.columns([2,2,2,2,2,2], gap='large')

    # with col1_header:
    #     st.image(r'img\logo_luminae.png', width=200)
    with col6_header:
        st.image(r'img\logo_luminae_gi.png', width=250)
    
    st.sidebar.image(r'img\logo_luminae.jpg')
    
    if st.sidebar.button("Página Inicial", key="inicio_button"):
        st.switch_page("Inicio.py")
    if st.sidebar.button("Categorizador IA", key="categorizador_button"):
        st.switch_page(r"pages\1_Categorizador.py")

    st.sidebar.image(r'img\img_luzia_acenando.png')
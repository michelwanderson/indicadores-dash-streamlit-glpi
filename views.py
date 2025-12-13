import streamlit as st
import plotly.express as px
from datetime import datetime
from plots import Filtro_Data, Dataframe_Retorno, Busca_Data_Hora_Modif



def Dataframe_Completo(Data_Inicial, Data_Final):
    df_completo = Filtro_Data(Dataframe_Retorno,Data_Inicial,Data_Final,'Data de abertura')[0]
    filtro = st.text_input("Filtro")

    if filtro:
        mask = df_completo.applymap(lambda x: filtro in str(x).lower()).any(axis=1)
        df_completo = df_completo[mask]


    st.data_editor(df_completo, hide_index=True,
        column_order=(
            "Título",
            "Localização",
            "Status",
            "Tempo de Abertura",
            "Data de abertura",
            "Requerente - Requerente",
            "Atribuído - Técnico",
            "ID"))




def Dataframe_Completo_html(Data_Inicial, Data_Final):
    df_completo = Filtro_Data(Dataframe_Retorno, Data_Inicial, Data_Final, 'Data de abertura')[0]
    filtro = st.text_input("Filtro")

    if filtro:
        mask = df_completo.applymap(lambda x: filtro in str(x).lower()).any(axis=1)
        df_completo = df_completo[mask]

    # Cria a coluna com hyperlink no ID
    df_completo["ID_Link"] = df_completo["ID"].apply(
        lambda x: f'<a href="https://endereço-glpi/front/ticket.form.php?id={x}" target="_blank">{x}</a>'
    )

    # Seleciona as colunas desejadas, substituindo o ID por ID_Link
    df_linkado = df_completo[[
        "Título",
        "Localização",
        "Status",
        "Data de abertura",
        "Requerente - Requerente",
        "Atribuído - Técnico",
        "ID_Link"
    ]].rename(columns={"ID_Link": "ID"})

    # Exibe como tabela com HTML renderizado
    df_linkado.to_html(escape=False, index=False, border=0)

    st.markdown(df_linkado.to_html(escape=False, index=False, border=0), unsafe_allow_html=True)
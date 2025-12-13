import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

from plots import Filtro_Data, Dataframe_Retorno, Busca_Data_Hora_Modif
from utils import Localizacao, Tecnicos, Requerentes, Categorias, Pareto_Categorias, Agrupamento_horas
from views import Dataframe_Completo, Dataframe_Completo_html



ARQUIVO_BASE = "Exemplo-Base.csv"
Dataframe_Retorno = pd.read_csv(ARQUIVO_BASE, sep=";")


##############                   Streamlit               ##############
st.title("Indicadores Infraestrutura 💹")


# --- MENU LATERAL ---
def Menu_Lateral():
    data_inicial, data_final = st.sidebar.date_input(
        "Selecione o intervalo de datas:",
        value=(datetime.today().date(), datetime.today().date())
    )

    data_inicial = data_inicial.strftime("%Y-%m-%d")
    data_final = data_final.strftime("%Y-%m-%d")

    st.sidebar.title('Menu de Navegação')
    Opcao_Escolha = st.sidebar.selectbox(
        'Escolha o gráfico:',
        [
            'Todos',
            'Localização',
            'Atribuição Técnica',
            'Requerente',
            'Categoria',
            'Categoria Pareto',
            'Horários',
            'Tabela',
            'Tabela Links',
            ])
    
    return data_inicial, data_final, Opcao_Escolha


# --- Execução do Menu Lateral ---
Data_Inicial, Data_Final, Opcao_Escolha = Menu_Lateral()


Total_de_Chamados = Filtro_Data(Dataframe_Retorno,Data_Inicial,Data_Final,'Data de abertura')[1]


# --- Quadros estaticos - Informações Gerais --- #
# Titulo
st.set_page_config(page_title="Infraestrutura - Indicadores", page_icon="💹", layout=None, initial_sidebar_state=None, menu_items=None)

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col1.metric("Data Inicial", f"{Data_Inicial}", border=True)
col3.metric("Data Final", f"{Data_Final}", border=True)
col2.metric("Total de Chamados", Total_de_Chamados, "", border=True)
col4.metric("Última Atualização da Base", Busca_Data_Hora_Modif(), border=True)





if Opcao_Escolha == 'Localização':
    Localizacao(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Atribuição Técnica':
    Tecnicos(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Requerente':
    Requerentes(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Categoria':
    Categorias(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Categoria Pareto':
    Pareto_Categorias(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Horários':
    Agrupamento_horas(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Tabela':
    Dataframe_Completo(Data_Inicial, Data_Final)

elif Opcao_Escolha == 'Tabela Links':
    Dataframe_Completo_html(Data_Inicial, Data_Final)

else:
    Localizacao(Data_Inicial, Data_Final)
    Tecnicos(Data_Inicial, Data_Final)
    Requerentes(Data_Inicial, Data_Final)
    Categorias(Data_Inicial, Data_Final)
    Agrupamento_horas(Data_Inicial, Data_Final)
    Dataframe_Completo(Data_Inicial, Data_Final)

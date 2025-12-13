import pandas as pd
from datetime import datetime
import subprocess
import streamlit as st


ARQUIVO_BASE = "Exemplo-Base.csv"
Dataframe_Retorno = pd.read_csv(ARQUIVO_BASE, sep=";")

# ---
@st.cache_data
def Filtro_Data(Df_Base, Data_Inicial, Data_Final, Coluna_Data_Filtro):
    Data_Inicial = pd.to_datetime(Data_Inicial)
    Data_Final = pd.to_datetime(Data_Final)

    Df_Base[Coluna_Data_Filtro] = pd.to_datetime(Df_Base[Coluna_Data_Filtro])

    # Expande o intervalo do mesmo dia, se Data_Inicial == Data_Final
    if Data_Inicial.date() == Data_Final.date():
        Data_Inicial = datetime.combine(Data_Inicial.date(), datetime.min.time())
        Data_Final = datetime.combine(Data_Final.date(), datetime.max.time())

    df_filtrado_data = Df_Base[(Df_Base[Coluna_Data_Filtro] >= Data_Inicial) & (Df_Base[Coluna_Data_Filtro] <= Data_Final)]
    df_contador = df_filtrado_data.shape[0]

    return df_filtrado_data, df_contador



@st.cache_data
def Busca_Data_Hora_Modif(nome_arquivo=ARQUIVO_BASE, arquivo="http://link-hospedagem-base-CSV"):

    comando = f"curl -s {arquivo} | grep {nome_arquivo} | awk \'{{print $3,$4}}\'"
    resultado_comando = subprocess.run([comando], shell=True, capture_output=True, text=True)


    return resultado_comando.stdout or "Indisponível"
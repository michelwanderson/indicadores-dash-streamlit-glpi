import pandas as pd
import plotly.express as px
from datetime import datetime
import streamlit as st
import plotly.graph_objects as go
from plots import Filtro_Data, Dataframe_Retorno



def Localizacao(Data_Inicial, Data_Final):
    df_localiz = Filtro_Data(
        Dataframe_Retorno,
        Data_Inicial,
        Data_Final,
        'Data de abertura')[0]
    Quant_Localiz = (df_localiz['Localização'].value_counts().reset_index())
    fig_localizacao = px.bar(
        Quant_Localiz,
        x='count',
        y='Localização',
        orientation='h',
        color_discrete_sequence=["#2BBFDA"],
        title='Distribuição por Localização')
    st.plotly_chart(fig_localizacao, key=f"localizacao-{Data_Inicial}-{Data_Final}")


def Tecnicos(Data_Inicial, Data_Final):
    def_tecnico = Filtro_Data(
        Dataframe_Retorno,
        Data_Inicial,
        Data_Final,
        'Data de abertura')[0]
    Quant_Tec = (
        def_tecnico['Atribuído - Técnico'].value_counts().reset_index())
    fig_tecnico = px.pie(
        Quant_Tec,
        values='count',
        names='Atribuído - Técnico',
        title='Distribuição por Técnico')
    st.plotly_chart(fig_tecnico, key=f"tecnicos-{Data_Inicial}-{Data_Final}")




# Tratamento com base de dados individual - Caso de atribuição dupla
# def Tecnicos():
#     def_tecnico = Filtro_Data(Dataframe_Retorno_Tecnicos,Data_Inicial,Data_Final,'Data de abertura')[0]
#     Quant_Tec = (def_tecnico['Atribuído - Técnico_y'].value_counts().reset_index())
#     fig_tecnico = px.pie(
#         Quant_Tec,
#         values='count',
#         names='Atribuído - Técnico_y',
#         title='Distribuição por Técnico')
#     st.plotly_chart(fig_tecnico)


def Requerentes(Data_Inicial, Data_Final):
    def_requerente = Filtro_Data(
        Dataframe_Retorno,
        Data_Inicial,
        Data_Final,
        'Data de abertura')[0]
    Quant_Req = (def_requerente['Requerente - Requerente'].value_counts().reset_index())
    Top_10_requerente = Quant_Req.nlargest(10, 'count')
    fig_requerente = px.bar(
        Top_10_requerente,
        x='Requerente - Requerente',
        y='count',
        color_discrete_sequence=['#FF5733'],
        title='Distribuição por Requerente')
    st.plotly_chart(fig_requerente, key=f"requerentes-{Data_Inicial}-{Data_Final}")



def Categorias(Data_Inicial, Data_Final):
    def_categoria = Filtro_Data(Dataframe_Retorno,Data_Inicial,Data_Final,'Data de abertura')[0]
    Quant_Categ = (def_categoria['Título'].value_counts().reset_index())
    Top_10_categorias = Quant_Categ.nlargest(10, 'count')
    fig_categorias = px.treemap(Top_10_categorias,
        # Hierarquia: aqui temos só um nível, por categoria
        path=['Título'],
        values='count',             # Tamanho de cada bloco
        color='count',              # Cor pode variar de acordo com a quantidade
        color_continuous_scale='Greens',
        # Paleta de cores (pode mudar pra Reds, Greens, etc.)
        title='Distribuição por Categoria'
    )
    st.plotly_chart(fig_categorias, key=f"categorias-{Data_Inicial}-{Data_Final}")






def Pareto_Categorias(Data_Inicial, Data_Final):
    # Dados filtrados
    df_categoria = Filtro_Data(Dataframe_Retorno, Data_Inicial, Data_Final, 'Data de abertura')[0]

    # Contagem por título
    contagem = df_categoria['Título'].value_counts().reset_index()
    contagem.columns = ['Título', 'Quantidade']
    contagem['% Acumulado'] = contagem['Quantidade'].cumsum() / contagem['Quantidade'].sum() * 100

    # Slider de controle
    max_categorias = min(30, len(contagem))
    n_categorias = st.slider("Número de categorias exibidas", 5, max_categorias, 10)

    # Subconjunto das N principais
    top_n = contagem.head(n_categorias)

    # Figura base
    fig = go.Figure()

    # Barras (quantidade)
    fig.add_trace(go.Bar(
        x=top_n['Título'],
        y=top_n['Quantidade'],
        name='Quantidade',
        marker_color='green',
        yaxis='y1'
    ))

    # Linha acumulada (%)
    fig.add_trace(go.Scatter(
        x=top_n['Título'],
        y=top_n['% Acumulado'],
        name='% Acumulado',
        yaxis='y2',
        mode='lines+markers',
        line=dict(color='orange', width=2)
    ))

    # ➕ Linha de corte em 80%
    fig.add_shape(
        type="line",
        x0=-0.5, y0=80,
        x1=len(top_n) - 0.5, y1=80,
        yref='y2',
        line=dict(
            color="red",
            width=2,
            dash="dash"
        )
    )

    # ➕ Anotação da linha de 80%
    fig.add_annotation(
        x=len(top_n) - 1,
        y=80,
        yref="y2",
        text="80% do total",
        showarrow=False,
        font=dict(color="red"),
        xanchor="left",
        yanchor="bottom"
    )

    # Layout geral
    fig.update_layout(
        title='Gráfico de Pareto das Categorias',
        xaxis=dict(title='Categoria'),
        yaxis=dict(title='Quantidade'),
        yaxis2=dict(
            title='% Acumulado',
            overlaying='y',
            side='right',
            range=[0, 110],
            showgrid=False
        ),
        legend=dict(x=0.75, y=1.15),
        margin=dict(t=40, b=80),
        height=500
    )

    st.plotly_chart(fig, key=f"pareto-{Data_Inicial}-{Data_Final}")




def Agrupamento_horas(Data_Inicial, Data_Final):
    df_agrup_horas = Filtro_Data(Dataframe_Retorno,Data_Inicial,Data_Final,'Data de abertura')[0]
    df_agrup_horas.loc[:, 'Data de abertura'] = pd.to_datetime(df_agrup_horas['Data de abertura'], dayfirst=False, errors='coerce')
    df_agrup_horas = df_agrup_horas.dropna(subset=['Data de abertura'])
    df_agrup_horas['Hora'] = df_agrup_horas['Data de abertura'].dt.hour

    contagem_hora = df_agrup_horas['Hora'].value_counts().sort_index().reset_index()

    fig = px.histogram(
        contagem_hora,
        x="Hora",
        y='count',
        color_discrete_sequence=px.colors.qualitative.Alphabet,
        nbins=50,
        title='Distribuição por Horário')

    st.plotly_chart(fig, key=f"horas-{Data_Inicial}-{Data_Final}")
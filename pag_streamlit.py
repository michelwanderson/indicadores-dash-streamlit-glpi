import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import os
import subprocess

URL = ""

Dataframe_Retorno = pd.read_csv(URL, sep=";")


##############                   Streamlit               ##############
st.title("Indicadores Infraestrutura - XXX Group")


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


def Localizacao():
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
    st.plotly_chart(fig_localizacao)


def Tecnicos():
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
    st.plotly_chart(fig_tecnico)


    Quant_Tec = (def_tecnico['Atribuído - Técnico'].value_counts().reset_index())
    fig_tecnico = px.pie(Quant_Tec,values='count',names='Atribuído - Técnico',title='Distribuição por Técnico')
    st.plotly_chart(fig_tecnico)


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





def Requerentes():
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
    st.plotly_chart(fig_requerente)



def Categorias():
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
    st.plotly_chart(fig_categorias)






def Pareto_Categorias():
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

    st.plotly_chart(fig)




def Agrupamento_horas():
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

    st.plotly_chart(fig)


def Dataframe_Completo():
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




def Dataframe_Completo_html():
    df_completo = Filtro_Data(Dataframe_Retorno, Data_Inicial, Data_Final, 'Data de abertura')[0]
    filtro = st.text_input("Filtro")

    if filtro:
        mask = df_completo.applymap(lambda x: filtro in str(x).lower()).any(axis=1)
        df_completo = df_completo[mask]

    # Cria a coluna com hyperlink no ID
    df_completo["ID_Link"] = df_completo["ID"].apply(
        lambda x: f'<a href="https://seu-link-glpi/front/ticket.form.php?id={x}" target="_blank">{x}</a>'
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




def Busca_Data_Hora_Modif(nome_arquivo="Base.txt", url="http://link-hospedagem-base-CSV:8080/glpi-api/dados/"):
    comando = f"curl -s {url} | grep {nome_arquivo} | awk \'{{print $3,$4}}\'"
    resultado_comando = subprocess.run([comando], shell=True, capture_output=True, text=True)

    return resultado_comando.stdout



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
    Localizacao()

elif Opcao_Escolha == 'Atribuição Técnica':
    Tecnicos()

elif Opcao_Escolha == 'Requerente':
    Requerentes()

elif Opcao_Escolha == 'Categoria':
    Categorias()

elif Opcao_Escolha == 'Categoria Pareto':
    Pareto_Categorias()

elif Opcao_Escolha == 'Horários':
    Agrupamento_horas()

elif Opcao_Escolha == 'Tabela':
    Dataframe_Completo()

elif Opcao_Escolha == 'Tabela Links':
    Dataframe_Completo_html()

else:
    Localizacao(), Tecnicos(), Requerentes(), Categorias(), Agrupamento_horas(), Dataframe_Completo()

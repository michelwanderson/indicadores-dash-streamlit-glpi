# 📊 Indicadores de Infraestrutura - GLPI Dashboard

![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-red.svg)
![Docker](https://img.shields.io/badge/docker-friendly-blue.svg)

Um painel de controle interativo construído com Streamlit para visualizar e analisar indicadores de chamados de TI, extraídos de uma instância GLPI.

---

## 📖 Sobre o Projeto

Este projeto oferece uma interface web para a equipe de infraestrutura da empresa XXX monitorar e analisar métricas de chamados. Ele permite a filtragem por período e a visualização de dados através de diversos gráficos e tabelas, facilitando a identificação de tendências, gargalos e a performance da equipe.

---

## ✨ Funcionalidades

O dashboard apresenta os seguintes indicadores e visualizações:

*   **Métricas Gerais:** Contagem total de chamados no período selecionado e data da última atualização da base de dados.
*   **Filtro por Data:** Selecione um intervalo de datas para analisar um período específico.
*   **Distribuição por Localização:** Gráfico de barras mostrando os locais com mais chamados.
*   **Atribuição por Técnico:** Gráfico de pizza com a distribuição de chamados entre os técnicos.
*   **Top 10 Requerentes:** Gráfico de barras com os usuários que mais abriram chamados.
*   **Distribuição por Categoria:** Treemap para visualizar as categorias de chamados mais comuns.
*   **Análise de Pareto por Categoria:** Gráfico de Pareto para identificar as categorias que representam 80% dos chamados.
*   **Distribuição por Horário:** Histograma que mostra os horários de pico na abertura de chamados.
*   **Tabela de Dados Completa:** Visualize, filtre e explore todos os dados brutos dos chamados.
*   **Tabela com Links:** Uma tabela que fornece links diretos para cada chamado na interface do GLPI.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

*   **Python 3.9**
*   **Streamlit:** Para a construção da interface web interativa.
*   **Pandas:** Para manipulação e análise dos dados.
*   **Plotly:** Para a criação dos gráficos interativos.
*   **Docker:** Para conteinerização e fácil deploy da aplicação.

---

## 🚀 Como Começar

Siga as instruções abaixo para executar o projeto em seu ambiente local.

### Pré-requisitos

*   [Python 3.9](https://www.python.org/downloads/)
*   [Docker](https://www.docker.com/get-started) (Recomendado para um setup mais fácil)
*   Um arquivo `requirements.txt` com as dependências do Python.

### Configuração

Antes de executar, é necessário configurar a fonte de dados.

1.  Abra o arquivo `pag_streamlit.py`.
2.  Altere a variável `URL` para o endereço do seu arquivo CSV de dados:
    ```python
    URL = "http://seu-servidor/caminho/para/o/arquivo.csv"
    ```

### 🏃 Executando Localmente (Sem Docker)

1.  Clone o repositório:
    ```sh
    git clone (https://github.com/michelwanderson/indicadores-dash-streamlit-glpi/)
    cd indicadores-dash-streamlit-glpi
    ```

2.  Crie e ative um ambiente virtual (recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4.  Execute a aplicação Streamlit:
    ```sh
    streamlit run pag_streamlit.py
    ```

A aplicação estará disponível em `http://localhost:8501`.

### 🐳 Executando com Docker

O `Dockerfile` fornecido simplifica a execução do projeto.

1.  Construa a imagem Docker:
    ```sh
    docker build -t indicadores-glpi .
    ```

2.  Execute o contêiner:
    ```sh
    docker run -p 8501:8501 indicadores-glpi
    ```

A aplicação estará disponível em `http://localhost:8501`.

<div id="top">

<!-- HEADER STYLE: COMPACT -->
<img src="readmeai/assets/logos/ice.svg" width="30%" align="left" style="margin-right: 15px">

# DASH_STREAMLIT_GLPI
<em>Um dashboard interativo para visualização de dados do GLPI, construído com Streamlit.</em>

<!-- BADGES -->
<img src="https://img.shields.io/git/license/wanderson.michel/dash_streamlit_glpi?style=flat-square&logo=opensourceinitiative&logoColor=white&color=E92063" alt="license">
<img src="https://img.shields.io/git/last-commit/wanderson.michel/dash_streamlit_glpi?style=flat-square&logo=git&logoColor=white&color=E92063" alt="last-commit">
<img src="https://img.shields.io/git/languages/top/wanderson.michel/dash_streamlit_glpi?style=flat-square&color=E92063" alt="repo-top-language">
<img src="https://img.shields.io/git/languages/count/wanderson.michel/dash_streamlit_glpi?style=flat-square&color=E92063" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=flat-square&logo=Plotly&logoColor=white" alt="Plotly">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas">

<br clear="left"/>

## 🌈 Table of Contents

<details>
<summary>Table of Contents</summary>

- [🌈 Table of Contents](#-table-of-contents)
- [🔴 Overview](#-overview)
- [🟠 Features](#-features)
- [🟡 Project Structure](#-project-structure)
    - [🟢 Project Index](#-project-index)
- [🔵 Getting Started](#-getting-started)
    - [🟣 Prerequisites](#-prerequisites)
    - [⚫ Installation](#-installation)
    - [⚪ Usage](#-usage)
    - [🟤 Testing](#-testing)
- [🌟 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 🔴 Visão Geral

O **DASH_STREAMLIT_GLPI** é uma aplicação web interativa para visualização de dados de uma instância GLPI. Construído com Streamlit e Plotly, ele oferece insights sobre o gerenciamento de ativos de TI e as operações de help desk. A aplicação é containerizada usando Docker para facilitar a implantação.

---

## 🟠 Features

- 📈 **Visualização de Dados Interativa**: Gráficos e tabelas dinâmicas para explorar os dados do GLPI.
- 🐳 **Containerização com Docker**: Implantação fácil e consistente em qualquer ambiente com Docker.
- 📊 **Análise de Chamados**: Dashboards para analisar chamados por status, categoria, técnico, e mais.
- 🔒 **Autenticação Segura**: (Opcional) Pode ser integrado com `streamlit-authenticator` para controle de acesso.

---

## 🟡 Project Structure

```sh
└── dash_streamlit_glpi/
    ├── Dockerfile
    ├── README.md
    ├── pag_streamlit.py
    └── requirements.txt
```

### 🟢 Project Index

<details open>
	<summary><b><code>DASH_STREAMLIT_GLPI/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://git.esig.group/wanderson.michel/dash_streamlit_glpi/-/blob/main/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>Define o ambiente e as dependências para construir a imagem Docker da aplicação.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://git.esig.group/wanderson.michel/dash_streamlit_glpi/-/blob/main/pag_streamlit.py'>pag_streamlit.py</a></b></td>
					<td style='padding: 8px;'>Script principal da aplicação Streamlit, contendo a lógica da interface e dos dashboards.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://git.esig.group/wanderson.michel/dash_streamlit_glpi/-/blob/main/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>Lista as dependências Python necessárias para executar o projeto.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🔵 Getting Started

### 🟣 Prerequisites

Este projeto requer as seguintes dependências:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker

### ⚫ Instalação

Build dash_streamlit_glpi from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://git.esig.group/wanderson.michel/dash_streamlit_glpi
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd dash_streamlit_glpi
    ```

3. **Instale as dependências:**

	Você pode instalar as dependências usando Docker (recomendado) ou localmente com Pip.

    **Opção 1: Usando Docker (Recomendado)**
    ```sh
    ❯ docker build -t dash-glpi .
    ```

    **Opção 2: Usando Pip (Ambiente Local)**
    ```sh
    ❯ pip install -r requirements.txt
    ```

### ⚪ Usage

Para executar o projeto:

**Com Docker:**
```sh
docker run -p 8501:8501 dash-glpi
```
Acesse o dashboard em `http://localhost:8501`.

**Localmente com Streamlit:**
```sh
streamlit run pag_streamlit.py
```

---

## 🌟 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://git.esig.group/wanderson.michel/dash_streamlit_glpi/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://git.esig.group/wanderson.michel/dash_streamlit_glpi/issues)**: Submit bugs found or log feature requests for the `dash_streamlit_glpi` project.
- **💡 [Submit Pull Requests](https://git.esig.group/wanderson.michel/dash_streamlit_glpi/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your git account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://git.esig.group/wanderson.michel/dash_streamlit_glpi
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to git**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://git.esig.group{/wanderson.michel/dash_streamlit_glpi/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=wanderson.michel/dash_streamlit_glpi">
   </a>
</p>
</details>

---

## 📜 License

Dash_streamlit_glpi is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---

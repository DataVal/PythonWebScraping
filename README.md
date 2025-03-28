# Web Scraper para Books to Scrape

## Sobre o Projeto
Este projeto foi desenvolvido como parte do meu aprendizado em web scraping, automação de tarefas e manipulação de dados com Python. Ele tem como objetivo coletar informações sobre livros de diferentes categorias disponíveis no site [Books to Scrape](https://books.toscrape.com/), armazenando os dados em uma planilha do Excel para análise posterior.

## Subprojetos de Aprendizado
Antes de construir este projeto principal, desenvolvi uma série de subprojetos para entender melhor cada uma das etapas envolvidas:

1. **Introdução ao Selenium**
   - Aprendi a abrir páginas da web e interagir com elementos usando Selenium.
   - Testei diferentes formas de localizar elementos (By.ID, By.CLASS_NAME, By.XPATH, etc.).

2. **Extração de Dados de Páginas Estáticas**
   - Desenvolvi scripts para extrair informações de páginas HTML estáticas utilizando BeautifulSoup.
   - Entendi a estrutura de páginas web e como navegar entre elementos usando seletores CSS.

3. **Paginação e Automação com Selenium**
   - Criei um scraper que percorria múltiplas páginas automaticamente.
   - Aprendi a lidar com botões "Next" e a esperar elementos carregarem antes de interagir.

4. **Manipulação de Planilhas com OpenPyXL**
   - Desenvolvi pequenos projetos para criar, modificar e salvar arquivos Excel.
   - Testei como armazenar dados extraídos diretamente em planilhas.

5. **Construção de uma Interface Gráfica com Tkinter e ttkbootstrap**
   - Experimentei a criação de interfaces interativas para facilitar a escolha de parâmetros do scraper.
   - Aprendi a conectar a GUI com o script principal para capturar as seleções do usuário.

## Projeto Principal: Web Scraper de Livros
### Funcionalidades
- Interface gráfica que permite ao usuário selecionar as categorias de livros que deseja extrair.
- Acesso automático ao site Books to Scrape, navegando por cada categoria selecionada.
- Coleta de informações como **nome do livro, preço, estoque e avaliação**.
- Paginação automática para garantir que todos os livros sejam coletados.
- Salvamento dos dados em uma planilha do Excel organizada por categorias.

### Tecnologias Utilizadas
- **Python** – Linguagem principal do projeto.
- **Selenium** – Automação da navegação e extração de dados da web.
- **OpenPyXL** – Manipulação de arquivos Excel.
- **ttkbootstrap** – Criação da interface gráfica para interação com o usuário.
- **WebDriver** – Utilizado para controle do navegador Chrome.

### Como Usar
#### Pré-requisitos
- Python instalado (versão 3.8 ou superior).
- Instalar as bibliotecas necessárias com:
  ```bash
  pip install selenium openpyxl ttkbootstrap
  ```
- Ter o WebDriver correspondente ao seu navegador instalado.

#### Execução
1. Execute o script principal para abrir a interface gráfica.
   ```bash
   python ScrapingLivrosBETA.py
   ```
2. Selecione as categorias desejadas e clique em "Confirmar Seleção".
3. Aguarde a coleta dos dados. O programa navegará pelas páginas e extrairá as informações.
4. O arquivo Excel gerado será salvo no mesmo diretório do script, contendo abas separadas para cada categoria.

---
Projeto desenvolvido para consolidar conhecimentos em Web Scraping e análise de dados.


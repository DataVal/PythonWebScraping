from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Configuração do WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Acessando o site
url = 'https://books.toscrape.com'
driver.get(url)

# Pegando os títulos e links dos livros
livros = driver.find_elements(By.CSS_SELECTOR, 'h3 a')
titulos = [livro.get_attribute('title') for livro in livros]
links = [livro.get_attribute('href') for livro in livros]

# Extraindo a quantidade de estoque
qtEstoque = []
for link in links:
    driver.get(link)
    estoque_texto = driver.find_element(By.CSS_SELECTOR, '.instock.availability').text
    estoque = int(estoque_texto.split('(')[-1].split()[0])  # Extração segura
    qtEstoque.append(estoque)

# Criando DataFrame
dfLivros = pd.DataFrame({"titulo": titulos, "estoque": qtEstoque})

# Exibir os dados
print(dfLivros)

# Fechar o driver
driver.quit()

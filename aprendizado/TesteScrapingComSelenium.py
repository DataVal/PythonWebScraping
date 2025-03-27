from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service,options=options)
url = 'https://books.toscrape.com'
driver.get(url)

livrosTitulos = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
titulo = [title.get_attribute('title') for title in livrosTitulos]
qtEstoque = []
for livro in livrosTitulos:
    livro.click()
    estoque = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
    qtEstoque.append(estoque)
    driver.back()

dictLivros = {"titulo": titulo,
              "estoque": qtEstoque}

#for i in range(len(dictLivros["titulo"])):
#    print(dictLivros["titulo"][i], dictLivros["estoque"][i])

dfLivros = pd.DataFrame(dictLivros)
print(dfLivros)
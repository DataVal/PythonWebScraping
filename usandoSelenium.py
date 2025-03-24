from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd

# O selenium difere do BeautifulSoup porque ele literalmente abre um navegador

#Uso da classe Service pra abrir uma instancia do chrome webdriver
service = Service()

#webdriver.options para definir preferencias para o browser do chrome
options = webdriver.ChromeOptions()

#Iniciamos a instância do Chrome Webdriver com as options e services
driver = webdriver.Chrome(service=service,options=options)
url = 'https://books.toscrape.com'
driver.get(url)

consultaTexto = driver.find_element(By.TAG_NAME, 'a').text

#Posso passar ao invés de text o atributo que quero
consultaTitulo = driver.find_element(By.TAG_NAME, 'a').get_attribute('title')

#Como sei que os elementos sobre os livros começam no a nº54 até o 92 posso fazer assim
#Tem que pular sempre pq entre uma tag 'a' e outra, tem uma tag dessa vazia
livros = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]

#Agora só preciso pegar o título de cada livro
titulos = [title.get_attribute('title') for title in livros]

print(titulos)

#Agora a grande diferença do BS4 pro Selenium
livrosParaClicar = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
livrosParaClicar[0].click()
# posso usar driver.back() para voltar na página

#Agora posso fazer algo mais bonitinho

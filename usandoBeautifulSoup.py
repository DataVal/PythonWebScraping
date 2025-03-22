import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://quotes.toscrape.com/') # Primeiro com a lib requests faço uma requisição get

dados_pagina = BeautifulSoup(pagina.text,'html.parser') # Crio uma instância do BS4 com o parser padrão de HTML

print(dados_pagina.prettify()) #Uso esse para ver de forma identada o código HMTL

#Aqui eu basicamente to dizendo: ache todos elemento HTML de tag 'div' que tenha a classe 'quote'
#A questão de ser 'class_' é porque class é palavra reservada do python para classes.
todas_frases = dados_pagina.find_all('div', class_="quote")
for div in todas_frases:
    texto = div.find('span', class_="text").text # O find vai achar o primeiro elemento que bater com os parâmetros da busca
    print(texto)

#Notas Extras
#O find aceita não somente parâmetros fixos, eu posso também passar funções
def filtroClasse(classe_qualquer):
    return classe_qualquer is not None and len(classe_qualquer) >= 9

divsfiltradas = dados_pagina.find_all('div', class_=filtroClasse)

for div in divsfiltradas:
    print(div['class'],div.text) #Outra coisa bacana é que eu posso acessar o valor de qualquer elemento usando suas propriedades
    print('---'*10)
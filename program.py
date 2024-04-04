import requests
from bs4 import BeautifulSoup

def extraitData():
    
    url_router = input("Veuillez entrer l'url du router:")
    response = requests.get(url_router)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        print(soup.prettify())
    else:
        print("echec de la requette", response.status_code)

extraitData()
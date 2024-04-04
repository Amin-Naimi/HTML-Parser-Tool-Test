import requests
from bs4 import BeautifulSoup

def extract_values():
    page_url = input("Veuillez entrer l'url de la page HTML: ")
    response = requests.get(page_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        pf_sys_value = soup.find('td', attrs={"name": "m1_3ph_pf_sys"}).text.strip()
        kwh_sys_value = soup.find('td', attrs={"name": "m1_3ph_kwh_sys"}).text.strip()
        kvar_sys_value = soup.find('td', attrs={"name": "m1_3ph_kvar_sys"}).text.strip()
        
        print("pf_sys:", pf_sys_value)
        print("kwh_sys:", kwh_sys_value)
        print("kvar_sys:", kvar_sys_value)
        
    else:
        print("*************__Error__*************")
        print("Échec de la requête:", response.status_code)
        print("*************__Error__*************")

extract_values()

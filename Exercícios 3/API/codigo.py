import requests
import json

def cotaçoes(moeda):
    try:
        moeda = moeda.upper()
        api = requests.get(f'https://economia.awesomeapi.com.br/last/{moeda}-BRL')
        api = api.json()
        cotaçao = float(api[f'{moeda}BRL']['bid'])
        return f'{moeda}: R${cotaçao:,.2f}'
    except:
        return None
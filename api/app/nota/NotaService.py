from requests import get
from bs4 import BeautifulSoup as bs
import re

class NotaService():
    def buscar(self, url:str) -> str:
        busca = get(url)
        busca.raise_for_status()

        return busca.text

    def scrape(self, conteudo:str) -> dict:
        expressao = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}'
        soup = bs(conteudo, 'lxml')

        retorno = {}

        try:
            # Pega de onde veio a compra
            lugar = soup.find('div', id='u20').text
            retorno['lugar'] = lugar

            # Pega data e hora
            div_data_hora = soup.find('div', id='infos').text
            texto_limpo = re.sub(r'\s+', ' ', div_data_hora)
            data_hora = re.findall(expressao, texto_limpo)
            retorno['data_hora'] = data_hora[0]

            # Pega valor da compra
            span_valor = soup.find('span', attrs={'class':'totalNumb txtMax'}).text
            retorno['valor'] = span_valor
            
            return retorno
        
        except Exception:
            print('Não foi possível econtrar a página em questão. Provavelmente a URL está errada.')
            raise


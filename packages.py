from datetime import datetime
import json
from struct import pack
import requests
import re
from bs4 import BeautifulSoup

class Packages:
    
    def write_json(file):
        """Retorna um arquivo json.
        
        :param file: list, dictionary, tuple.
        """
        
        # Cria o arquivo json.
        with open('data.json', 'w+') as f:
            json.dump(file, f, ensure_ascii=False, indent=1, separators=(',', ':'))
    
    
    def web_scraping():
        """ Função que irá retornar um web scraping de um site e transformar os dados em um arquivo json.
        """

        # Usa a biblioteca requests para pegar a url do site a ser acessado.
        page = requests.get('https://www.contabeis.com.br/conteudo/contabil/')
      
        # Extrai o conteúdo da págia em html.
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Lista que irá ser convertida em Json.
        data = ['data:']
        
        
        # Vai extrair os dados pela quantidade de artigos presentes na página.
        for c in range(len(soup.find_all('article', class_='editoria-contabil'))):
            # Pega o link da postagem baseado na tag "ul" e classe "compartilhamento".
            pub_link = soup.find_all('ul', class_='compartilhamento', attrs={'href': re.compile("^https://")})[c]
            
            # Pega o horário da publicação do site.
            time = soup.find_all('em', class_='timestamp')[c].text
            
            # Converte o formato do horário para horas/mintos e segundos, se tiver.
            if 'Ontem' in time:
                # Pega o texto a partir do sexto caractere da classe "timestamp" do atributo "em".
                time = soup.find_all('em', class_='timestamp')[c].text[6::]
                
                if len(time) > 5:
                    time_format = datetime.strptime(time, '%H:%M:%S')
                    time = time_format.strftime('%H:%M:%S')
                else:
                    time_format = datetime.strptime(time, '%H:%M')
                    time = time_format.strftime('%H:%M')
            else:
                time = soup.find_all('em', class_='timestamp')[c].text[11::]
                
                if len(time) > 5:
                    time_format = datetime.strptime(time, '%H:%M:%S')
                    time = time_format.strftime('%H:%M:%S')
                else:
                    time_format = datetime.strptime(time, '%H:%M')
                    time = time_format.strftime('%H:%M')
                
            # Dicionário com as informações extraídas do site .   
            dictionary = { 
                'title': soup.find_all('h2')[c].text, 
                'category':soup.find_all('strong')[c].text, 
                'time': time,
                'link': pub_link.get("href"),
                }
            
            # Adiciona o dicionário a uma lista.
            data.append(dictionary)
        
        # Adiciona a quantidade de assuntos presentes, levando em consideração a quantidade de vezes que a classe aparece.
        data.append(f'size: {len(soup.find_all("article", class_="editoria-contabil"))}')
        
        # Cria o arquivo json.
        Packages.write_json(data)
        
        

                
            
        
        


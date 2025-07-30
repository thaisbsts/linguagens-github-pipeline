import requests
import pandas as pd
import os

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv('API_KEY')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                    'X-GitHub-Api-Version': '2022-11-28'}

    def get_repositories_list(self):
        repos_list = []
        page_num = 1

        while True:
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                data = response.json()

                # Verifica se veio uma lista vazia (página sem repositórios)
                if not data:
                    break

                repos_list.append(data) # Se não tiver vazia, adiciona na lista
                page_num += 1 # Incrementa para ir na página seguinte na próxima iteração
            except Exception as e:
                break  

        return repos_list


    def get_repos_names(self, repos_list): 
        repo_names = [] 
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except: 
                    pass

        return repo_names

    def get_repos_languages(self, repos_list):
        repo_languages = []
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass
 
        return repo_languages

    def create_languages_df(self):
        repositorios = self.get_repositories_list()
        nomes = self.get_repos_names(repositorios)
        linguagens = self.get_repos_languages(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados


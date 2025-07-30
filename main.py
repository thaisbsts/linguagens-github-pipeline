import os
from dotenv import load_dotenv
from dados_repositorios import DadosRepositorios
from manipula_repositorios import ManipulaRepositorios 

load_dotenv()

company_users = ['amzn', 'netflix', 'spotify', 'apple']

for company_user in company_users:
    company_rep = DadosRepositorios(company_user)
    repos_languages = company_rep.create_languages_df()
    repos_languages.to_csv(f'dados/languages_{company_user}')

    # new_rep = ManipulaRepositorios('thaisbsts')
    # rep_name = 'companies-repositories-languages'
    # new_rep.cria_repo(rep_name)
    # new_rep.add_arquivo(rep_name, f'languages_{company_user}.csv', f'languages_{company_user}.csv')
    
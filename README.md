# ETL de Linguagens de Programação no GitHub
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![dotenv](https://img.shields.io/badge/dotenv-000.svg?style=for-the-badge&logo=dotenv&logoColor=white)

<p align="center">
  <a href="#general">Informações Gerais</a> • 
  <a href="#aboutproject">Especificação do Projeto</a> • 
  <a href="#technologies">Tecnologias Utilizadas</a> • 
  <a href="#projectstructure">Estrutura do Projeto</a>
</p>


<h2 id="general">🚀 Informações Gerais</h2>

Este projeto foi desenvolvido no curso 'Python e APIs: conhecendo a biblioteca Requests' da formação 'Primeiros passos com Engenharia de Dados' oferecido pela Alura. O curso aborda integração com APIs utilizando Python, abordando autenticação, paginação, métodos HTTP (GET, POST, PUT e DELETE), interpretação de status codes, manipulação de dados com bibliotecas como Requests e Pandas, além de reforçar conceitos fundamentais de programação orientada a objetos.

<h2 id="aboutproject">📋 Especificação do Projeto</h2>

A proposta do projeto é construir um pipeline ETL para extrair informações públicas da API do GitHub, com foco nas linguagens utilizadas em repositórios das empresas **Amazon**, **Apple**, **Netflix** e **Spotify**.

- No estágio inicial (notebook linguagens_repos.ipynb), foi feito um processo manual para a empresa Amazon.
- Em seguida, o código foi refatorado e generalizado com Programação Orientada a Objetos (POO) para suportar múltiplas empresas.
- Os dados extraídos são transformados e exportados para arquivos .csv, armazenados na pasta dados/.

<h2 id="technologies">🛠 Tecnologias Utilizadas</h2>

- Python 3
- Requests – para comunicação com a API do GitHub
- Pandas – para manipulação e exportação dos dados
- dotenv – para gerenciamento de variáveis de ambiente (token de autenticação)
- Jupyter Notebook – para exploração inicial da biblioteca Requests
- Git e GitHub – para versionamento do código

<h2 id="projectstructure">📁 Estrutura do Projeto</h2>

```

├── dados/                      # CSVs gerados com os dados de cada empresa
│   ├── languages_amzn.csv
│   ├── languages_apple.csv
│   ├── languages_netflix.csv
│   └── languages_spotify.csv
│
├── linguagens_repos.ipynb     # Desenvolvimento inicial da pipeline (caso da Amazon)
├── dados_repositorios.py      # Classe para obter dados da API do GitHub
├── manipula_repositorios.py   # Classe para tratamento e exportação dos dados
├── main.py                    # Script principal que executa o ETL completo
├── requirements.txt           # Bibliotecas necessárias
├── .gitignore
└── README.md                  # Este arquivo

```

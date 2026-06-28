# Gerador de Testes Academicos - Ensino Medio

Sistema automatizado para geracao de cadernos de testes dinamicos de Matematica e Fisica, desenvolvido para a plataforma do SENAI Gama (Desenvolvimento de Sistemas).

## Tecnologias Utilizadas
* Linguagem: Python 3 (gerenciando pacotes locais em ambiente virtual .venv).
* Framework Web: Flask (responsavel pelas rotas, controle de sessoes e renderizacao de templates HTML).
* Banco de Dados: SQLite (gerenciado pelo modulo local banco para salvar historicos e gabaritos).
* Interface (Frontend): HTML5 estilizado com Bootstrap 5 (comportamento dinamico via JavaScript nativo para troca de materias).
* Renderizacao Grafica: Matplotlib (configurada com o backend Agg para gerar graficos de Cinematica em background de forma assincrona, convertendo-os em strings Base64 injetadas direto no HTML).

## Arquitetura do Projeto
O projeto segue um padrao modular focado em separacao de responsabilidades (Clean Architecture):

`	ext
gerador-testes-matematica/
├── .venv/                   # Ambiente virtual isolado
├── templates/
│   └── index.html           # Frontend (Bootstrap 5 + Seleção dinâmica)
├── src/
│   ├── app.py               # Controlador principal (Rotas Flask /gerar e /corrigir)
│   ├── banco.py             # Camada de Persistência (Conexão e Tabelas SQLite)
│   ├── matematica.py        # Módulo gerador de questões algébricas
│   ├── graficos_fisica.py   # Motor gráfico (Matplotlib -> Base64)
│   └── fisica/              # Módulo de Física totalmente componentizado
│       ├── __init__.py      # Inicializador do pacote de física
│       ├── cinematica.py    # Gerador de MRU com gráficos acoplados
│       ├── vetores.py       # Questões vetoriais textuais
│       └── ... (dinamica, energia, etc.)
├── .gitignore               # Proteção para não subir arquivos locais/lixo
└── requirements.txt         # Dependências do projeto (Flask, Matplotlib)
`",
",


1. Ative o ambiente virtual no terminal:
   .venv\Scripts\activate

2. Instale todas as dependencias necessarias do sistema:
   pip install -r requirements.txt

3. Inicialize o servidor local do Flask:
   python src/app.py

4. Abra o seu navegador e acesse o endereco: http://127.0.0.1:5000

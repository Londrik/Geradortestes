# Gerador de Testes Acadêmicos - Ensino Médio

Sistema automatizado para geração de cadernos de testes dinâmicos de Matemática e Física, desenvolvido para a plataforma do SENAI Gama (Desenvolvimento de Sistemas).

## Tecnologias Utilizadas
* Linguagem: Python 3 (gerenciando pacotes locais em ambiente virtual .venv).
* Framework Web: Flask (responsável pelas rotas, controle de sessões e renderização de templates HTML).
* Banco de Dados: SQLite (gerenciado pelo módulo local banco para salvar históricos e gabaritos).
* Interface (Frontend): HTML5 estilizado com Bootstrap 5 (comportamento dinâmico via JavaScript nativo para troca de matérias).
* Renderização Gráfica: Matplotlib (configurada com o backend Agg para gerar gráficos de Cinemática em background de forma assíncrona, convertendo-os em strings Base64 injetadas direto no HTML).

## Arquitetura do Projeto
O projeto segue um padrão modular focado em separação de responsabilidades (Clean Architecture):

```text
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
```

## Como Executar o Ambiente Local

1. Ative o ambiente virtual no terminal:
```powershell
.venv\Scripts\activate
```

2. Instale todas as dependências necessárias do sistema:
```powershell
pip install -r requirements.txt
```

3. Inicialize o servidor local do Flask:
```powershell
python src/app.py
```

4. Abra o seu navegador e acesse o endereço: `http://127.0.0.1:5000`

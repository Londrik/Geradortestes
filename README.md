# Gerador de Testes Academicos - Ensino Medio

Sistema automatizado para geracao de cadernos de testes dinamicos de Matematica e Fisica, desenvolvido para a plataforma do SENAI Gama (Desenvolvimento de Sistemas).

## Tecnologias Utilizadas
* Linguagem: Python 3 (gerenciando pacotes locais em ambiente virtual .venv).
* Framework Web: Flask (responsavel pelas rotas, controle de sessoes e renderizacao de templates HTML).
* Banco de Dados: SQLite (gerenciado pelo modulo local banco para salvar historicos e gabaritos).
* Interface (Frontend): HTML5 estilizado com Bootstrap 5 (comportamento dinamico via JavaScript nativo para troca de materias).
* Renderizacao Grafica: Matplotlib (configurada com o backend Agg para gerar graficos de Cinematica em background de forma assincrona, convertendo-os em strings Base64 injetadas direto no HTML).

## Arquitetura do Projeto
O projeto segue um erro padrao modular focado em separacao de responsabilidades (Clean Architecture):

- .venv/ (Ambiente virtual isolado)
- templates/index.html (Frontend Bootstrap 5 + Selecao dinamica)
- src/app.py (Controlador principal - Rotas Flask /gerar e /corrigir)
- src/banco.py (Camada de Persistencia - Conexao e Tabelas SQLite)
- src/matematica.py (Modulo gerador de questoes algebricas)
- src/graficos_fisica.py (Motor grafico - Matplotlib para Base64)
- src/fisica/ (Modulo de Fisica totalmente componentizado)
- .gitignore (Protecao para nao subir arquivos locais e lixo)
- requirements.txt (Dependencias do projeto)

## Como Executar o Ambiente Local

1. Ative o ambiente virtual no terminal:
   .venv\Scripts\activate

2. Instale todas as dependencias necessarias do sistema:
   pip install -r requirements.txt

3. Inicialize o servidor local do Flask:
   python src/app.py

4. Abra o seu navegador e acesse o endereco: http://127.0.0.1:5000

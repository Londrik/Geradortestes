

```markdown

\# Gerador de Testes de Matemática



Este projeto consiste em uma aplicação web desenvolvida em Python com o ecossistema Flask para a geração automatizada, renderização e correção de testes de matemática. A arquitetura foi projetada seguindo princípios de modularidade, separação de conceitos (Separation of Concerns) e funções puras, operando sem o uso de Mapeamento Objeto-Relacional (ORM) ou Programação Orientada a Objetos (POO).



\## Arquitetura do Sistema



A árvore de diretórios do projeto segue estritamente a estrutura modular abaixo:



```text

gerador-testes-matematica/

│

├── src/

│   ├── app.py             # Servidor web e controle de rotas HTTP (Flask)

│   ├── banco.py           # Camada de persistência (Funções puras via mysql.connector)

│   └── matematica.py      # Motor matemático (Geração algorítmica de equações e aritmética)

│

├── templates/

│   ├── exercicio.html     # Interface do teste (Bootstrap, Flexbox e Jinja2)

│   └── resultado.html     # Tela de feedback e computação de acertos pós-correção

│

├── .gitignore

├── README.md

└── requirements.txt       # Dependências do projeto (Flask, mysql-connector-python)



```



\---



\## Engenharia Reversa e Lógica de Geração dos Cálculos



O arquivo `src/matematica.py` encapsula a lógica determinística e pseudoaleatória (utilizando a biblioteca nativa `random`) para garantir que cada teste possua desafios únicos, com alternativas geradas dinamicamente e sem colisões de respostas.



\### 1. Operações Aritméticas Básicas



\* \*\*Definição:\*\* Geração de operações binárias de soma, subtração, multiplicação e divisão.

\* \*\*Mecanismo:\*\* Define-se um intervalo numérico para os operandos $A$ e $B$ (ex: $\[1, 100]$). O operador é selecionado aleatoriamente.

\* \*\*Divisão Controlada:\*\* Para garantir que o teste apresente divisões exatas (divisores inteiros), o sistema gera primeiro o quociente $Q$ e o divisor $B$. O dividendo é calculado como $A = B \\times Q$. Assim, a operação apresentada é $A \\div B = Q$, eliminando dízimas periódicas e restos na folha de testes.



\### 2. Equações polinomiais de 1º Grau



\* \*\*Estrutura:\*\* Expressões na forma padrão $ax + b = c$.

\* \*\*Mecanismo de Geração:\*\* 1. Define-se o valor da raiz $x$ de forma oculta e aleatória dentro de um intervalo inteiro (ex: $\[-10, 10]$, excluindo o zero).

2\. Definem-se os coeficientes inteiros $a$ e $b$.

3\. O valor constante $c$ é computado estritamente por avaliação direta: $c = (a \\cdot x) + b$.

4\. A equação é exibida para o aluno ocultando-se a incógnita $x$, garantindo que a resposta final seja sempre um número inteiro dedutível.



\### 3. Equações polinomiais de 2º Grau



\* \*\*Estrutura:\*\* Expressões na forma $ax^2 + bx + c = 0$.

\* \*\*Mecanismo de Geração (Raízes Inteiras Garantidas):\*\* Em vez de gerar coeficientes aleatórios e aplicar a fórmula de Bhaskara (correndo o risco de gerar discriminantes ($\\Delta$) negativos ou raízes irracionais), o motor utiliza o processo reverso através do Teorema de Viète ou fatoração de polinômios:

1\. Sorteiam-se duas raízes inteiras independentes, $x\_1$ e $x\_2$.

2\. Define-se o coeficiente principal $a$ (geralmente $a = 1$).

3\. Expandem-se os fatores: $a(x - x\_1)(x - x\_2) = ax^2 - a(x\_1 + x\_2)x + ax\_1x\_2$.

4\. Os coeficientes finais são mapeados como:

\* $b = -a(x\_1 + x\_2)$

\* $c = a \\cdot x\_1 \\cdot x\_2$





5\. A equação final $ax^2 + bx + c = 0$ é exibida, assegurando que o conjunto solução pertença estritamente aos números inteiros ($\\mathbb{Z}$).







\### Geração de Distratores (Alternativas Incorretas)



Para cada questão, a resposta correta é inserida em uma lista ao lado de três distratores. Os distratores são gerados adicionando ou subtraindo offsets aleatórios da resposta correta, garantindo que não haja duplicidade no conjunto de opções. A lista final de quatro opções é embaralhada (`random.shuffle`) antes de ser injetada no template.



\---



\## Camada de Persistência e Integração MySQL



O módulo `src/banco.py` realiza o mapeamento de dados bruto utilizando o driver `mysql.connector`. A conexão gerencia transações diretamente através de comandos SQL ANSI puros, sem abstrações de alta camada.



\* \*\*Isolamento de Escopo:\*\* Toda consulta abre uma conexão, executa a instrução por meio de um cursor, realiza o `commit` (se necessário) e fecha os recursos imediatamente em blocos estruturados de tratamento de exceções.

\* \*\*Controle de Escopo de Loops no Jinja2:\*\* No front-end (`templates/exercicio.html`), para evitar o acoplamento de estados ao renderizar inputs do tipo `radio` aninhados, o índice da questão pai é fixado no escopo do loop utilizando a tag `{% set pergunta\_idx = loop.index0 %}`. Isso garante o isolamento do atributo `name="q{{ pergunta\_idx }}"` em conformidade com o interpretador de templates.



\---



\## Tecnologias Utilizadas



\* \*\*Linguagem:\*\* Python 3.12+

\* \*\*Framework Web:\*\* Flask (Engenharia de Rotas e Middleware)

\* \*\*Template Engine:\*\* Jinja2 (Renderização Dinâmica Server-Side)

\* \*\*Driver de Banco de Dados:\*\* `mysql-connector-python`

\* \*\*Estilização UI:\*\* Bootstrap 5.3 (Layout via Flexbox utilitário, sem injeção de scripts JavaScript no cliente)



```



```


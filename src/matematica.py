import random  # CORREÇÃO: Adicionado o import que faltava


def formata_br(numero):
    return f"{numero:.2f}".rstrip("0").rstrip(".").replace(".", ",")


def gerar_opcoes(correta, tipo="int"):
    erros = set()  # Usando set para evitar alternativas duplicadas automaticamente

    if tipo == "dec":
        # Opções baseadas em erros comuns
        potenciais = [
            correta + 1.5,
            correta - 1.5,
            correta + 0.5,
            correta - 0.5,
            correta * 2,
        ]
        for e in potenciais:
            if e > 0 and round(e, 2) != round(correta, 2):
                erros.add(formata_br(e))

        # Se não encheu as 3 opções, gera valores aleatórios incrementais
        while len(erros) < 3:
            novo_erro = correta + random.choice([0.1, 0.5, 1.2, 2.5])
            if round(novo_erro, 2) != round(correta, 2) and novo_erro > 0:
                erros.add(formata_br(novo_erro))

        return list(erros)[:3]

    else:
        correta_int = int(correta)
        potenciais = [
            correta_int + 2,
            correta_int - 2,
            correta_int + 5,
            correta_int - 3,
            correta_int * 2,
        ]
        for e in potenciais:
            if e != correta_int and e > 0:
                erros.add(str(e))

        # CORREÇÃO: Garante o preenchimento sem duplicar e sem loop infinito
        while len(erros) < 3:
            novo_erro = correta_int + random.randint(3, 15)
            if novo_erro != correta_int and novo_erro > 0:
                erros.add(str(novo_erro))

        return list(erros)[:3]


def definir_limites(dificuldade):
    """Retorna multiplicadores ou ranges baseados no nível selecionado."""
    if d := dificuldade.lower():
        if "facil" in d:
            return 1, 5
        if "dificil" in d:
            return 3, 20
        if "avancado" in d:
            return 5, 50
    return 2, 12  # Intermediário


# ==================== REVISÃO & FUNDAMENTOS ====================


def modulo_aritmetica(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    # 5 de Multiplicação
    for _ in range(5):
        a = round(random.uniform(min_val, max_val), 1)
        b = round(random.uniform(min_val, max_val / 2 + 2), 1)
        correta = round(a * b, 2)
        opcoes = [formata_br(correta)] + gerar_opcoes(correta, "dec")
        random.shuffle(opcoes)
        questoes.append(
            {
                "enunciado": f"Quanto é {formata_br(a)} vezes {formata_br(b)}?",
                "correta": formata_br(correta),
                "alternativas": opcoes,
            }
        )

    # 5 de Divisão
    for _ in range(5):
        resp = round(random.uniform(min_val, max_val), 1)
        b = round(random.uniform(min_val + 1, max_val / 2 + 2), 1)
        a = round(resp * b, 2)
        opcoes = [formata_br(resp)] + gerar_opcoes(resp, "dec")
        random.shuffle(opcoes)
        questoes.append(
            {
                "enunciado": f"Quanto é {formata_br(a)} dividido por {formata_br(b)}?",
                "correta": formata_br(resp),
                "alternativas": opcoes,
            }
        )
    return questoes


def modulo_conjuntos(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    for i in range(10):
        a = random.randint(min_val, max_val)
        b = a + random.randint(min_val + 2, max_val + 5)

        if i % 2 == 0:
            pergunta = f"Dado o intervalo fechado A = [{a}, {b}], qual dos seguintes números pertence a A?"
            correta = random.randint(a, b)
            erros = {a - 1, b + 1, a - 3, b + 5}
        else:
            pergunta = f"Dado o conjunto B com os elementos formado por x > {a} e x <= {b}. Qual número NÃO pertence a B?"
            correta = a
            erros = {random.randint(a + 1, b), b, a + 2}

        # CORREÇÃO: Remove a possibilidade do elemento correto ser sorteado como erro acidentalmente
        erros_filtrados = [str(e) for e in erros if e != correta]
        while len(erros_filtrados) < 3:
            erros_filtrados.append(str(b + random.randint(6, 12)))

        opcoes = [str(correta)] + random.sample(erros_filtrados, 3)
        random.shuffle(opcoes)
        questoes.append(
            {"enunciado": pergunta, "correta": str(correta), "alternativas": opcoes}
        )
    return questoes


# ==================== FUNÇÕES (1º E 2º GRAU) ====================


# CORREÇÃO: Renomeado de modulo_funcoes para modulo_funcao_afim para sincronizar com seu app.py
def modulo_funcao_afim(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    for _ in range(5):
        a, b = random.randint(min_val + 1, max_val), random.randint(1, max_val * 2)
        x = random.randint(1, 6)
        correta = (a * x) + b
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append(
            {
                "enunciado": f"Dada a função f(x) = {a}x + {b}, qual é o valor numérico de f({x})?",
                "correta": str(correta),
                "alternativas": opcoes,
            }
        )

    for _ in range(5):
        a = random.randint(min_val + 1, max_val)
        b = random.randint(1, max_val * 2)

        if random.choice([True, False]):
            pergunta = (
                f"Na função f(x) = {a}x + {b}, identifique o Coeficiente Angular (a):"
            )
            correta = a
        else:
            pergunta = (
                f"Na função f(x) = {a}x + {b}, identifique o Coeficiente Linear (b):"
            )
            correta = b
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append(
            {"enunciado": pergunta, "correta": str(correta), "alternativas": opcoes}
        )
    return questoes


def modulo_quadratica(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    for _ in range(5):
        a = random.randint(1, max(2, min_val))
        b = random.randint(1, max_val)
        c = random.randint(1, max_val)
        x = random.randint(1, 4)
        correta = (a * (x**2)) + (b * x) + c
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append(
            {
                "enunciado": f"Dada a função f(x) = {a}x² + {b}x + {c}, qual é o valor de f({x})?",
                "correta": str(correta),
                "alternativas": opcoes,
            }
        )

    for _ in range(5):
        a = random.randint(1, max_val)
        b = random.randint(1, max_val)
        c = random.randint(1, max_val)
        pergunta = f"Na função f(x) = {a}x² + {b}x + {c}, qual é o coeficiente do termo quadrático (a)?"
        opcoes = [str(a)] + gerar_opcoes(a, "int")
        random.shuffle(opcoes)
        questoes.append(
            {"enunciado": pergunta, "correta": str(a), "alternativas": opcoes}
        )
    return questoes


# ==================== ÁLGEBRA AVANÇADA ====================


def modulo_inequacoes(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    for i in range(10):
        a = random.randint(2, max_val)
        b = random.randint(min_val, max_val * 2)
        c = a * random.randint(1, 5)

        if i % 2 == 0:
            correta_val = (c + b) // a
            pergunta = f"Resolva a inequação linear: {a}x - {b} > {c}"
            correta = f"x > {correta_val}"
            erros = [
                f"x < {correta_val}",
                f"x > {correta_val + 2}",
                f"x < {correta_val - 1}",
            ]
        else:
            correta_val = (c - b) // a
            pergunta = f"Resolva a inequação linear: {a}x + {b} <= {c}"
            correta = f"x <= {correta_val}"
            erros = [
                f"x >= {correta_val}",
                f"x <= {correta_val + 3}",
                f"x > {correta_val - 2}",
            ]

        opcoes = [correta] + erros
        random.shuffle(opcoes)
        questoes.append(
            {"enunciado": pergunta, "correta": correta, "alternativas": opcoes}
        )
    return questoes


def modulo_sequencias(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    for i in range(10):
        a1 = random.randint(min_val, max_val)
        r = random.randint(2, min_val + 5)

        if i % 2 == 0:  # P.A.
            termo_num = random.randint(4, 6)
            correta = a1 + (termo_num - 1) * r
            seq_str = f"({a1}, {a1 + r}, {a1 + r * 2}, ...)"
            pergunta = f"Determine o {termo_num}º termo da Progressão Aritmética (P.A.): {seq_str}"
            erros = [str(correta + r), str(correta - r), str(correta + 2)]
        else:  # P.G.
            q = random.choice([2, 3])
            termo_num = 4
            correta = a1 * (q ** (termo_num - 1))
            seq_str = f"({a1}, {a1 * q}, {a1 * q * 2 if q == 2 else a1 * q * q}, ...)"
            pergunta = f"Determine o {termo_num}º termo da Progressão Geométrica (P.G.): {seq_str}"
            erros = [str(correta + 5), str(correta * q), str(correta // q)]

        opcoes = [str(correta)] + erros
        random.shuffle(opcoes)
        questoes.append(
            {"enunciado": pergunta, "correta": str(correta), "alternativas": opcoes}
        )
    return questoes


# ==================== APLICAÇÕES PRÁTICAS ====================


def modulo_financeira(dificuldade="intermediario"):
    questoes = []
    min_val, max_val = definir_limites(dificuldade)

    for _ in range(10):
        porcentagem = random.choice([10, 20, 25, 50, 15, 30])
        if "dificil" in dificuldade.lower():
            porcentagem = random.choice([7, 13, 21, 35])

        total_dinheiro = random.randint(min_val * 10, max_val * 20)
        correta = (porcentagem * total_dinheiro) / 100

        pergunta = f"Quanto é {porcentagem}% de R$ {total_dinheiro},00?"
        opcoes = [formata_br(correta)] + gerar_opcoes(correta, "dec")
        random.shuffle(opcoes)
        questoes.append(
            {
                "enunciado": pergunta,
                "correta": formata_br(correta),
                "alternativas": opcoes,
            }
        )
    return questoes


def modulo_trigonometria(dificuldade="intermediario"):
    questoes = []

    banco_trig = [
        {
            "enunciado": "Em um triângulo retângulo, qual a razão do Cateto Oposto pela Hipotenusa?",
            "correta": "Seno",
            "alternativas": ["Seno", "Cosseno", "Tangente", "Secante"],
        },
        {
            "enunciado": "Qual a razão trigonométrica que representa o Cateto Adjacente dividido pela Hipotenusa?",
            "correta": "Cosseno",
            "alternativas": ["Seno", "Cosseno", "Tangente", "Cotangente"],
        },
        {
            "enunciado": "Qual o valor do Seno de 30 graus?",
            "correta": "1/2",
            "alternativas": ["1/2", "Raiz de 2 / 2", "Raiz de 3 / 2", "1"],
        },
        {
            "enunciado": "Qual o valor do Cosseno de 60 graus?",
            "correta": "1/2",
            "alternativas": ["1/2", "Raiz de 3 / 2", "0", "Raiz de 2 / 2"],
        },
        {
            "enunciado": "Qual o valor da Tangente de 45 graus?",
            "correta": "1",
            "alternativas": ["1", "0", "Raiz de 3", "Raiz de 3 / 3"],
        },
        {
            "enunciado": "Se um triângulo retângulo possui hipotenusa 10 e um dos ângulos agudos é de 30°, qual o valor do cateto oposto a esse ângulo?",
            "correta": "5",
            "alternativas": ["5", "5 √3", "10", "2,5"],
        },
        {
            "enunciado": "A soma dos ângulos internos de qualquer triângulo plano é sempre igual a:",
            "correta": "180°",
            "alternativas": ["180°", "90°", "360°", "270°"],
        },
        {
            "enunciado": "O Teorema de Pitágoras afirma que o quadrado da hipotenusa é igual à:",
            "correta": "Soma dos quadrados dos catetos",
            "alternativas": [
                "Soma dos quadrados dos catetos",
                "Diferença dos catetos",
                "Multiplicação dos catetos",
                "Raiz quadrada dos catetos",
            ],
        },
        {
            "enunciado": "Em um triângulo retângulo, se os catetos medem 3 e 4, quanto mede a hipotenusa?",
            "correta": "5",
            "alternativas": ["5", "7", "12", "25"],
        },
        {
            "enunciado": "Qual a razão trigonométrica equivalente a Cateto Oposto dividido por Cateto Adjacente?",
            "correta": "Tangente",
            "alternativas": ["Tangente", "Seno", "Cosseno", "Cossecante"],
        },
    ]

    if "dificil" in dificuldade.lower() or "avancado" in dificuldade.lower():
        banco_trig[8] = {
            "enunciado": "Em um triângulo retângulo, se os catetos medem 6 e 8, quanto mede a hipotenusa?",
            "correta": "10",
            "alternativas": ["10", "14", "48", "100"],
        }

    return random.sample(banco_trig, 10)

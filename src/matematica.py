import random

def formata_br(numero):
    return f"{numero:.2f}".rstrip('0').rstrip('.').replace('.', ',')

def gerar_opcoes(correta, tipo="int"):
    if tipo == "dec":
        erros = {correta + 1.5, correta - 1.5, correta + 0.5, correta - 0.5, correta * 2}
        erros = [e for e in erros if e > 0 and round(e, 2) != round(correta, 2)]
        while len(erros) < 3:
            erros.append(correta + random.choice([0.1, 0.5, 1.2]))
        return [formata_br(e) for e in random.sample(erros, 3)]
    else:
        erros = {correta + 2, correta - 2, correta + 5, correta - 3, correta * 2}
        erros = [e for e in erros if e != correta]
        while len(erros) < 3:
            erros.append(correta + random.randint(3, 10))
        return [str(e) for e in random.sample(erros, 3)]

def modulo_aritmetica():
    questoes = []
    for _ in range(5):
        a, b = round(random.uniform(1.5, 9.5), 1), round(random.uniform(1.5, 5.5), 1)
        correta = round(a * b, 2)
        opcoes = [formata_br(correta)] + gerar_opcoes(correta, "dec")
        random.shuffle(opcoes)
        questoes.append({"pergunta": f"Quanto é {formata_br(a)} vezes {formata_br(b)}?", "correta": formata_br(correta), "opcoes": opcoes})
    for _ in range(5):
        resp = round(random.uniform(1.5, 9.5), 1)
        b = round(random.uniform(2, 5), 1)
        a = round(resp * b, 2)
        opcoes = [formata_br(resp)] + gerar_opcoes(resp, "dec")
        random.shuffle(opcoes)
        questoes.append({"pergunta": f"Quanto é {formata_br(a)} dividido por {formata_br(b)}?", "correta": formata_br(resp), "opcoes": opcoes})
    return questoes

def modulo_funcoes():
    questoes = []
    for _ in range(5):
        a, b = random.randint(2, 5), random.randint(1, 10)
        x = random.randint(1, 6)
        correta = (a * x) + b
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append({"pergunta": f"Dada a função f(x) = {a}x + {b}, qual é o valor numérico de f({x})?", "correta": str(correta), "opcoes": opcoes})
    for _ in range(5):
        a, b = random.randint(2, 9), random.randint(1, 15)
        if random.choice([True, False]):
            pergunta = f"Na função f(x) = {a}x + {b}, identifique o Coeficiente Angular (a):"
            correta = a
        else:
            pergunta = f"Na função f(x) = {a}x + {b}, identifique o Coeficiente Linear (b):"
            correta = b
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append({"pergunta": pergunta, "correta": str(correta), "opcoes": opcoes})
    return questoes

def modulo_quadratica():
    questoes = []
    for _ in range(5):
        a, b, c, x = random.randint(2, 4), random.randint(1, 5), random.randint(1, 6), random.randint(2, 4)
        correta = (a * (x ** 2)) + (b * x) + c
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append({"pergunta": f"Dada a função f(x) = {a}x² + {b}x + {c}, qual é o valor de f({x})?", "correta": str(correta), "opcoes": opcoes})
    for _ in range(5):
        a, b, c = random.randint(2, 9), random.randint(1, 12), random.randint(1, 15)
        opcoes = [str(a)] + gerar_opcoes(a, "int")
        random.shuffle(opcoes)
        questoes.append({"pergunta": f"Na função f(x) = {a}x² + {b}x + {c}, qual é o coeficiente do termo quadrático (a)?", "correta": str(a), "opcoes": opcoes})
    return questoes
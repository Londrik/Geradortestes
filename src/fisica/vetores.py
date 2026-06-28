import random

def definir_limites(dificuldade):
    if d := difficulty.lower() if (difficulty := dificuldade) else "":
        if "facil" in d: return 1, 4
        if "dificil" in d: return 5, 15
        if "avancado" in d: return 10, 30
    return 2, 8

def modulo_fundamentos_vetores(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for i in range(5):  # Gerando 5 questões focadas
        f1 = random.randint(min_v * 2, max_v * 2)
        f2 = random.randint(min_v * 2, max_v * 2)
        
        if i % 2 == 0:
            correta = f1 + f2
            pergunta = f"Dois vetores de forças possuem a mesma direção e o mesmo sentido, medindo {f1} N e {f2} N. Qual o módulo do vetor resultante?"
            resolucao = f"Como os vetores possuem a mesma direção e o mesmo sentido, somamos seus módulos: R = F1 + F2 => R = {f1} + {f2} = {correta} N."
        else:
            correta = abs(f1 - f2)
            if correta == 0: correta = f1
            pergunta = f"Dois vetores de forças possuem a mesma direção, mas sentidos opostos, medindo {f1} N e {f2} N. Qual o módulo do vetor resultante?"
            resolucao = f"Como os vetores possuem sentidos opostos, subtraímos seus módulos (valor absoluto): R = |F1 - F2| => R = |{f1} - {f2}| = {correta} N."
        
        erros = {correta + 2, correta - 2, correta + 10, correta * 2}
        erros = [e for e in erros if e != correta and e > 0]
        while len(erros) < 3:
            erros.append(correta + random.randint(3, 15))
        opcoes = [str(correta)] + [str(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        
        questoes.append({
            "enunciado": pergunta, 
            "correta": str(correta), 
            "alternativas": opcoes,
            "resolucao": resolucao
        })
    return questoes

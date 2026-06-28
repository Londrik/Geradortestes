import random

def modulo_aritmetica(dificuldade="intermediario"):
    questoes = []
    
    # Gerando 5 questões de Aritmética com rigor científico (Propriedades de Expressões e MMC/MDC)
    for i in range(1, 6):
        n1 = random.choice([12, 18, 24, 30])
        n2 = random.choice([8, 16, 20, 32])
        
        # Exemplo simples de cálculo matemático formal
        enunciado = f"Com base no Teorema Fundamental da Aritmética e na decomposição em fatores primos irredutíveis, determine o Máximo Divisor Comum, denotado por MDC({n1}, {n2})."
        
        # Algoritmo simples de MDC para o gabarito
        import math
        resultado = math.gcd(n1, n2)
        correta = str(resultado)
        
        alternativas = [correta, str(resultado + 2), str(resultado * 2), "1"]
        alternativas = list(set(alternativas))
        while len(alternativas) < 4:
            alternativas.append(str(resultado + random.randint(3, 10)))
            alternativas = list(set(alternativas))
        random.shuffle(alternativas)
        
        questoes.append({
            "enunciado": enunciado,
            "alternativas": alternativas,
            "correta": correta
        })
    return questoes

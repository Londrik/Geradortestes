import random

def modulo_quadratica(dificuldade="intermediario"):
    questoes = []
    
    for _ in range(5):
        a = random.choice([1, 2, 3, 4, 5])
        b = random.randint(1, 20)
        c = random.randint(1, 45)
        x = random.randint(1, 4)
        resultado = a * (x ** 2) + b * x + c
        
        enunciado = f"Pelo Teorema Fundamental do Cálculo Algébrico aplicado a polinômios de segundo grau P(x) = ax² + bx + c, determine a imagem do elemento x = {x} pertencente ao domínio real da função f(x) = {a}x² + {b}x + {c}."
        correta = str(resultado)
        
        alternativas = [correta, str(resultado + random.randint(2, 10)), str(resultado - random.randint(2, 8)), str(resultado * 2)]
        alternativas = list(set(alternativas))
        while len(alternativas) < 4:
            alternativas.append(str(resultado + random.randint(11, 20)))
            alternativas = list(set(alternativas))
        random.shuffle(alternativas)
        
        questoes.append({"enunciado": enunciado, "alternativas": alternativas, "correta": correta})
        
    for _ in range(5):
        a = random.randint(2, 50)
        b = random.randint(2, 50)
        c = random.randint(1, 50)
        
        enunciado = f"Dada a assinatura estrutural de uma função quadrática f: ℝ → ℝ definida por f(x) = ax² + bx + c, extraia o coeficiente do termo dominante de maior grau (a) para a lei de formação f(x) = {a}x² + {b}x + {c}."
        correta = str(a)
        
        alternativas = [correta, str(b), str(c), str(a * 2)]
        alternativas = list(set(alternativas))
        while len(alternativas) < 4:
            alternativas.append(str(a + random.randint(1, 10)))
            alternativas = list(set(alternativas))
        random.shuffle(alternativas)
        
        questoes.append({"enunciado": enunciado, "alternativas": alternativas, "correta": correta})
        
    return questoes

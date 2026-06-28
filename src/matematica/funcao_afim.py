import random

def modulo_funcao_afim(dificuldade="intermediario"):
    questoes = []
    for i in range(1, 6):
        a = random.choice([2, 3, 4, 5])
        b = random.choice([1, 6, 7, 10])
        x = random.randint(1, 4)
        resultado = a * x + b
        
        enunciado = f"Com base na definição formal de uma transformação afim f(x) = ax + b linearmente transladada, calcule a imagem f({x}) sob o mapeamento f(x) = {a}x + {b}."
        correta = str(resultado)
        
        alternativas = [correta, str(resultado + random.randint(2, 5)), str(resultado - random.randint(2, 4)), str(a + b)]
        alternativas = list(set(alternativas))
        while len(alternativas) < 4:
            alternativas.append(str(resultado + random.randint(6, 12)))
            alternativas = list(set(alternativas))
        random.shuffle(alternativas)
        
        questoes.append({"enunciado": enunciado, "alternativas": alternativas, "correta": correta})
    return questoes

import random

def definir_limites(dificuldade):
    if d := difficulty.lower() if (difficulty := dificuldade) else "":
        if "facil" in d: return 1, 4
        if "dificil" in d: return 5, 15
        if "avancado" in d: return 10, 30
    return 2, 8

def modulo_dinamica_leis_newton(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for _ in range(10):
        m = random.randint(min_v * 2, max_v * 4)
        a = random.randint(2, 6)
        f = m * a
        erros = {f + 2, f - 2, f + 10, f * 2}
        erros = [e for e in erros if e != f and e > 0]
        while len(erros) < 3:
            erros.append(f + random.randint(3, 15))
        opcoes = [str(f)] + [str(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um bloco de massa {m} kg é puxado em uma superfície horizontal sem atrito, adquirindo uma aceleração de {a} m/s². Qual a intensidade da força resultante?",
            "correta": str(f),
            "alternativas": opcoes,
        })
    return questoes

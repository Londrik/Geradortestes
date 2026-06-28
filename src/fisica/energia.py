import random

def definir_limites(dificuldade):
    if d := difficulty.lower() if (difficulty := dificuldade) else "":
        if "facil" in d: return 1, 4
        if "dificil" in d: return 5, 15
        if "avancado" in d: return 10, 30
    return 2, 8

def modulo_trabalho_energia(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for _ in range(5):
        f = random.randint(10, 10 + min_v * 10)
        d = random.randint(2, 10)
        t = f * d
        erros = {t + 2, t - 2, t + 10, t * 2}
        erros = [e for e in erros if e != t and e > 0]
        while len(erros) < 3:
            erros.append(t + random.randint(3, 15))
        opcoes = [str(t)] + [str(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Uma força constante de {f} N empurra um caixote por uma distância de {d} metros na mesma direção da força. Calcule o trabalho realizado.",
            "correta": str(t),
            "alternativas": opcoes,
        })
    for _ in range(5):
        m = random.randint(2, 6)
        h = random.randint(2, 10)
        g = 10
        ep = m * g * h
        erros = {ep + 2, ep - 2, ep + 10, ep * 2}
        erros = [e for e in erros if e != ep and e > 0]
        while len(erros) < 3:
            erros.append(ep + random.randint(3, 15))
        opcoes = [str(ep)] + [str(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um vaso de massa {m} kg está posicionado no topo de um armário a {h} metros de altura. Considerando g = 10 m/s², qual a energia potencial gravitacional do vaso?",
            "correta": str(ep),
            "alternativas": opcoes,
        })
    return questoes

import random

def formata_br(numero):
    return f"{numero:.2f}".rstrip("0").rstrip(".").replace(".", ",")

def modulo_impulso_colisoes(dificuldade="intermediario"):
    questoes = []
    for _ in range(10):
        f = random.randint(20, 40)
        dt = round(random.uniform(0.1, 0.5), 2)
        i = round(f * dt, 2)
        erros = {i + 1.5, i - 1.5, i + 0.5, i * 2}
        erros = [e for e in erros if e > 0 and round(e, 2) != round(i, 2)]
        while len(erros) < 3:
            erros.append(i + random.choice([0.1, 0.5, 1.2]))
        opcoes = [formata_br(i)] + [formata_br(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um jogador de futebol chuta uma bola aplicando uma força média de {f} N durante um intervalo de tempo de {formata_br(dt)} segundos. Qual o módulo do impulso exercido na bola?",
            "correta": formata_br(i),
            "alternativas": opcoes,
        })
    return questoes

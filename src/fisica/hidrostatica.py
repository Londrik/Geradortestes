import random

def modulo_hidrostatica_empuxo(dificuldade="intermediario"):
    questoes = []
    for _ in range(10):
        f = random.randint(10, 50)
        area = random.choice([2, 5, 10])
        p = f // area
        erros = {p + 2, p - 2, p + 10, p * 2}
        erros = [e for e in erros if e != p and e > 0]
        while len(erros) < 3:
            erros.append(p + random.randint(3, 15))
        opcoes = [str(p)] + [str(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Uma força perpendicular de {f} N é aplicada uniformemente sobre uma placa de área {area} m². Qual é a pressão exercida sobre essa placa em N/m²?",
            "correta": str(p),
            "alternativas": opcoes,
        })
    return questoes

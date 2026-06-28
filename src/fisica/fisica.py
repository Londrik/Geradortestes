import random
import math

def formata_br(numero):
    return f"{numero:.2f}".rstrip("0").rstrip(".").replace(".", ",")

def gerar_opcoes(correta, tipo="int"):
    if tipo == "dec":
        erros = {
            correta + 1.5,
            correta - 1.5,
            correta + 0.5,
            correta - 0.5,
            correta * 2,
        }
        erros = [e for e in erros if e > 0 and round(e, 2) != round(correta, 2)]
        while len(erros) < 3:
            erros.append(correta + random.choice([0.1, 0.5, 1.2]))
        return [formata_br(e) for e in random.sample(erros, 3)]
    else:
        correta_int = int(correta)
        erros = {correta_int + 2, correta_int - 2, correta_int + 10, correta_int * 2}
        erros = [e for e in erros if e != correta_int and e > 0]
        while len(erros) < 3:
            erros.append(correta_int + random.randint(3, 15))
        return [str(e) for e in random.sample(erros, 3)]

def definir_limites(dificuldade):
    if d := difficulty.lower() if (difficulty := dificuldade) else "":
        if "facil" in d:
            return 1, 4
        if "dificil" in d:
            return 5, 15
        if "avancado" in d:
            return 10, 30
    return 2, 8

def modulo_fundamentos_vetores(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for i in range(10):
        f1 = random.randint(min_v * 2, max_v * 2)
        f2 = random.randint(min_v * 2, max_v * 2)
        if i % 2 == 0:
            correta = f1 + f2
            pergunta = f"Dois vetores de forças possuem a mesma direção e o mesmo sentido, medindo {f1} N e {f2} N. Qual o módulo do vetor resultante?"
        else:
            correta = abs(f1 - f2)
            if correta == 0:
                correta = f1
            pergunta = f"Dois vetores de forças possuem a mesma direção, mas sentidos opostos, medindo {f1} N e {f2} N. Qual o módulo do vetor resultante?"
        opcoes = [str(correta)] + gerar_opcoes(correta, "int")
        random.shuffle(opcoes)
        questoes.append({"enunciado": pergunta, "correta": str(correta), "alternativas": opcoes})
    return questoes

def modulo_cinematica_mru_mruv(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for i in range(5):
        v = random.randint(min_v * 5, max_v * 5)
        t = random.randint(2, 5)
        d = v * t
        opcoes = [str(d)] + gerar_opcoes(d, "int")
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um veículo trafega com velocidade constante de {v} m/s em uma rodovia (MRU). Qual a distância percorrida por ele após {t} segundos?",
            "correta": str(d),
            "alternativas": opcoes,
        })
    for _ in range(5):
        a = random.randint(1, min_v + 1)
        t = random.randint(2, 4)
        v_final = a * t
        opcoes = [str(v_final)] + gerar_opcoes(v_final, "int")
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um carro parte do repouso e acelera constantemente a {a} m/s² (MRUV). Qual será sua velocidade após {t} segundos?",
            "correta": str(v_final),
            "alternativas": opcoes,
        })
    return questoes

def modulo_dinamica_leis_newton(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for _ in range(10):
        m = random.randint(min_v * 2, max_v * 4)
        a = random.randint(2, 6)
        f = m * a
        opcoes = [str(f)] + gerar_opcoes(f, "int")
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um bloco de massa {m} kg é puxado em uma superfície horizontal sem atrito, adquirindo uma aceleração de {a} m/s². Qual a intensidade da força resultante?",
            "correta": str(f),
            "alternativas": opcoes,
        })
    return questoes

def modulo_trabalho_energia(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for _ in range(5):
        f = random.randint(10, 10 + min_v * 10)
        d = random.randint(2, 10)
        t = f * d
        opcoes = [str(t)] + gerar_opcoes(t, "int")
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
        opcoes = [str(ep)] + gerar_opcoes(ep, "int")
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um vaso de massa {m} kg está posicionado no topo de um armário a {h} metros de altura. Considerando g = 10 m/s², qual a energia potencial gravitacional do vaso?",
            "correta": str(ep),
            "alternativas": opcoes,
        })
    return questoes

def modulo_impulso_colisoes(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for _ in range(10):
        f = random.randint(20, 20 + min_v * 10)
        dt = round(random.uniform(0.1, 0.5), 2)
        i = round(f * dt, 2)
        opcoes = [formata_br(i)] + gerar_opcoes(i, "dec")
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Um jogador de futebol chuta uma bola aplicando uma força média de {f} N durante um intervalo de tempo de {formata_br(dt)} segundos. Qual o módulo do impulso exercido na bola?",
            "correta": formata_br(i),
            "alternativas": opcoes,
        })
    return questoes

def modulo_estatica_gravitacao(dificuldade="intermediario"):
    questoes = []
    banco_estatica = [
        {
            "enunciado": "A Primeira Lei de Kepler estabelece que as órbitas dos planetas ao redor do Sol possuem formato:",
            "correta": "Elíptico",
            "alternativas": ["Elíptico", "Circular Perfeito", "Retilíneo", "Parabólico"],
        },
        {
            "enunciado": "Para que um corpo rígido extenso esteja em completo equilíbrio estático, além da força resultante ser nula, o que mais deve ser nulo?",
            "correta": "O torque (momento) resultante",
            "alternativas": ["O torque (momento) resultante", "A massa do objeto", "A aceleração da gravidade", "A velocidade angular inicial"],
        },
        {
            "enunciado": "Uma barra homogênea de peso desprezível está apoiada no centro. Se colocarmos um peso de 20 N a 2 metros do centro na esquerda, a que distância da direita devemos colocar um peso de 40 N para equilibrar a barra?",
            "correta": "1",
            "alternativas": ["1", "2", "4", "0,5"],
        },
        {
            "enunciado": "Quem propôs a Lei da Gravitação Universal, determinando que matéria atrai matéria na razão inversa do quadrado da distância?",
            "correta": "Isaac Newton",
            "alternativas": ["Isaac Newton", "Johannes Kepler", "Galileu Galilei", "Albert Einstein"],
        }
    ]
    while len(questoes) < 10:
        alvo = random.choice(banco_estatica)
        clone = alvo.copy()
        opts = list(clone["alternativas"])
        random.shuffle(opts)
        clone["alternativas"] = opts
        questoes.append(clone)
    return questoes

def modulo_hidrostatica_empuxo(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    for _ in range(10):
        f = random.randint(10, 10 + min_v * 5)
        area = random.choice([2, 5, 10])
        p = f // area
        opcoes = [str(p)] + gerar_opcoes(p, "int")
        random.shuffle(opcoes)
        questoes.append({
            "enunciado": f"Uma força perpendicular de {f} N é aplicada uniformemente sobre uma placa de área {area} m². Qual é a pressão exercida sobre essa placa em N/m²?",
            "correta": str(p),
            "alternativas": opcoes,
        })
    return questoes

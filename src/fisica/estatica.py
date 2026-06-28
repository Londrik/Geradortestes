import random

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

import random

def modulo_conjuntos(dificuldade="intermediario"):
    questoes = []
    for i in range(1, 6):
        enunciado = f"Utilizando a álgebra booleana e a teoria dos conjuntos, aplique o operador de união unária (A ∪ B) sobre os intervalos contínuos na reta real definidos por A = {{x ∈ ℝ | 1 ≤ x ≤ {i+2}}} e B = {{x ∈ ℝ | {i} ≤ x ≤ 5}}."
        correta = f"[1, 5]"
        alternativas = [correta, f"[1, {i}]", f"[{i}, {i+2}]", "Ø"]
        random.shuffle(alternativas)
        questoes.append({"enunciado": enunciado, "alternativas": alternativas, "correta": correta})
    return questoes

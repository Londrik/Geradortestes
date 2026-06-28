import random
import graficos_fisica

def definir_limites(dificuldade):
    d = dificuldade.lower() if dificuldade else ""
    if "facil" in d: 
        return 1, 4
    if "dificil" in d: 
        return 5, 15
    if "avancado" in d: 
        return 10, 30
    return 2, 8

def modulo_cinematica_mru_mruv(dificuldade="intermediario"):
    questoes = []
    min_v, max_v = definir_limites(dificuldade)
    
    for _ in range(5):
        v = random.randint(min_v * 4, max_v * 4)
        t = random.randint(3, 6)
        d = v * t  
        
        imagem_grafico = graficos_fisica.gerar_grafico_mru(v, t)
        
        pergunta = f"Analise o gráfico de velocidade em função do tempo gerado abaixo para um veículo em movimento uniforme. Com base na propriedade geométrica da área sob a curva, determine a distância total percorrida pelo móvel entre os instantes 0s e {t}s."
        resolucao = f"Em um gráfico v x t, a distância percorrida é numericamente igual à área sob a linha. A figura gerada forma um retângulo de base = {t} e altura = {v}. Portanto: Área = base × altura => d = {t} × {v} = {d} metros."
        
        erros = {d + 5, d - 5, d + 20, d * 2}
        erros = [e for e in erros if e != d and e > 0]
        while len(erros) < 3:
            erros.append(d + random.randint(6, 25))
            
        opcoes = [str(d)] + [str(e) for e in random.sample(erros, 3)]
        random.shuffle(opcoes)
        
        questoes.append({
            "enunciado": pergunta,
            "imagem": imagem_grafico,  
            "correta": str(d),
            "alternativas": opcoes,
            "resolucao": resolucao
        })
    return questoes

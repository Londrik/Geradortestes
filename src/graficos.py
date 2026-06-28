import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import random

def gerar_grafico_base64_2grau(a, b, c):
    plt.figure(figsize=(5, 4))
    xv = -b / (2 * a)
    x = [xv + delta for delta in [i * 0.1 for i in range(-50, 51)]]
    y = [a * (val ** 2) + b * val + c for val in x]
    
    plt.plot(x, y, color='blue', linewidth=2)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title(f"Gráfico de f(x)")
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return img_base64

def formatar_vertice(x, y):
    # Arredonda para no máximo 2 casas decimais para sumir com as dízimas longas
    x_formatado = round(x, 2) if not x.is_integer() else int(x)
    y_formatado = round(y, 2) if not y.is_integer() else int(y)
    return f"V({x_formatado}, {y_formatado})"

def gerar_questao_2grau_grafico():
    a = random.choice([1, 2, 3])
    b = random.choice([-4, -2, 0, 2, 4])
    c = random.choice([-3, -1, 1, 3])
    
    xv = -b / (2 * a)
    yv = -(b**2 - 4*a*c) / (4*a)
    
    imagem = gerar_grafico_base64_2grau(a, b, c)
    
    enunciado = "O gráfico abaixo representa uma função quadrática f(x) = ax² + bx + c. Analisando a parábola, determine as coordenadas do seu vértice V(xv, yv)."
    
    # Usa o formatador para deixar as alternativas limpas
    correta = formatar_vertice(xv, yv)
    alternativas = [
        correta,
        formatar_vertice(xv + 1, yv),
        formatar_vertice(xv, yv - 2),
        formatar_vertice(-xv, -yv)
    ]
    # Remove duplicatas se houverem antes de embaralhar
    alternativas = list(set(alternativas))
    while len(alternativas) < 4:
        alternativas.append(formatar_vertice(xv + random.randint(2, 5), yv + random.randint(2, 5)))
        alternativas = list(set(alternativas))
        
    random.shuffle(alternativas)
    
    return {
        "enunciado": enunciado,
        "imagem_base64": imagem,
        "alternativas": alternativas,
        "correta": correta
    }

def gerar_questao_1grau_grafico():
    plt.figure(figsize=(5, 4))
    a = random.choice([-2, -1, 1, 2])
    b = random.choice([-3, -1, 1, 3])
    
    x = list(range(-5, 6))
    y = [a * val + b for val in x]
    
    plt.plot(x, y, color='red', linewidth=2)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    imagem = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    
    enunciado = "Determine o coeficiente linear (interseção com o eixo y) da reta representada no gráfico abaixo:"
    correta = str(b)
    
    alternativas = [correta, str(b + 1), str(-b), str(a)]
    alternativas = list(set(alternativas))
    while len(alternativas) < 4:
        alternativas.append(str(b + random.randint(2, 5)))
        alternativas = list(set(alternativas))
    random.shuffle(alternativas)
    
    return {
        "enunciado": enunciado,
        "imagem_base64": imagem,
        "alternativas": alternativas,
        "correta": correta
    }

from flask import Flask, render_template, request, redirect
import matematica
import banco
import graficos
import unicodedata

app = Flask(__name__, template_folder="../templates")

banco.criar_tabelas()

def remover_acentos(texto):
    if not texto:
        return ""
    return "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar", methods=["POST"])
def gerar():
    materia_opcao = request.form.get("materia")
    dificuldade_bruta = request.form.get("dificuldade", "intermediario")
    dificuldade = remover_acentos(dificuldade_bruta)

    questoes = []
    titulo = ""
    usar_graficos = "dificil" in dificuldade or "avancado" in dificuldade

    if materia_opcao == "conjuntos":
        titulo = "Conjuntos Numéricos e Intervalos"
        questoes = matematica.modulo_conjuntos(dificuldade=dificuldade)

    elif materia_opcao == "aritmetica":
        titulo = "Aritmética e Teoria dos Números"
        questoes = matematica.modulo_aritmetica(dificuldade=dificuldade)

    elif materia_opcao == "funcao_afim":
        titulo = "Função de 1º Grau (Afim)"
        if usar_graficos:
            func_1g = getattr(graficos, "gerar_questao_1grau_grafico", None) or getattr(graficos, "gerar_grafico_1grau", None)
            questoes = [func_1g() for _ in range(5)] if func_1g else list(matematica.modulo_funcao_afim(dificuldade=dificuldade))
        else:
            questoes = list(matematica.modulo_funcao_afim(dificuldade=dificuldade))

    elif materia_opcao == "funcao_quadratica":
        titulo = "Função de 2º Grau (Quadrática)"
        if usar_graficos:
            func_2g = getattr(graficos, "gerar_questao_2grau_grafico", None) or getattr(graficos, "gerar_grafico_2grau", None)
            questoes = [func_2g() for _ in range(5)] if func_2g else list(matematica.modulo_quadratica(dificuldade=dificuldade))
        else:
            questoes = list(matematica.modulo_quadratica(dificuldade=dificuldade))

    if not questoes:
        return redirect("/")

    respostas_chave = "|".join([q["correta"] for q in questoes])
    id_teste = banco.salvar_gabarito(titulo, dificuldade_bruta, respostas_chave)

    return render_template(
        "teste.html", titulo=titulo, questoes=questoes, id_teste=id_teste
    )

@app.route("/corrigir", methods=["POST"])
def corrigir():
    id_teste = request.form.get("id_teste")
    gabarito_string = banco.buscar_gabarito(id_teste)
    
    if not gabarito_string:
        return "Gabarito não encontrado no sistema.", 404
        
    respostas_corretas = gabarito_string.split("|")
    total_questoes = len(respostas_corretas)
    acertos = 0
    
    for i in range(total_questoes):
        resposta_aluno = request.form.get(f"questao_{i}")
        if resposta_aluno == respostas_corretas[i]:
            acertos += 1
            
    nota = (acertos / total_questoes) * 10
    
    return f"""
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h2>Resultado da Correção (Teste #{id_teste})</h2>
        <p style="font-size: 20px;">Você acertou <strong>{acertos}</strong> de <strong>{total_questoes}</strong> questões.</p>
        <h1 style="color: {'green' if nota >= 6 else 'red'}; font-size: 48px;">Nota: {nota:.1f}</h1>
        <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #004b87; color: white; text-decoration: none; border-radius: 4px; font-weight: bold;">Voltar ao Início</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)

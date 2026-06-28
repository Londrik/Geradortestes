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
    
    # Transforma "difícil" em "dificil" e "avançado" em "avancado"
    dificuldade = remover_acentos(dificuldade_bruta)

    questoes = []
    titulo = ""
    
    # Verifica se deve gerar gráficos
    usar_graficos = "dificil" in dificuldade or "avancado" in dificuldade

    # 1. MATÉRIA: CONJUNTOS
    if materia_opcao == "conjuntos":
        titulo = "Conjuntos Numéricos e Intervalos"
        questoes = matematica.modulo_conjuntos(dificuldade=dificuldade)

    # 2. MATÉRIA: FUNÇÃO DE 1º GRAU (AFIM)
    elif materia_opcao == "funcao_afim":
        titulo = "Função de 1º Grau (Afim)"
        if usar_graficos:
            func_1g = getattr(graficos, "gerar_questao_1grau_grafico", None) or getattr(graficos, "gerar_grafico_1grau", None)
            if func_1g:
                questoes = [func_1g() for _ in range(5)]
            else:
                questoes = list(matematica.modulo_funcao_afim(dificuldade=dificuldade))
        else:
            questoes = list(matematica.modulo_funcao_afim(dificuldade=dificuldade))

    # 3. MATÉRIA: FUNÇÃO DE 2º GRAU (QUADRÁTICA)
    elif materia_opcao == "funcao_quadratica":
        titulo = "Função de 2º Grau (Quadrática)"
        if usar_graficos:
            func_2g = getattr(graficos, "gerar_questao_2grau_grafico", None) or getattr(graficos, "gerar_grafico_2grau", None)
            if func_2g:
                questoes = [func_2g() for _ in range(5)]
            else:
                questoes = list(matematica.modulo_quadratica(dificuldade=dificuldade))
        else:
            questoes = list(matematica.modulo_quadratica(dificuldade=dificuldade))

    if not questoes:
        return redirect("/")

    respostas_chave = ",".join([q["correta"] for q in questoes])
    id_teste = banco.salvar_gabarito(titulo, dificuldade_bruta, respostas_chave)

    return render_template(
        "teste.html", titulo=titulo, questoes=questoes, id_teste=id_teste
    )


if __name__ == "__main__":
    app.run(debug=True)

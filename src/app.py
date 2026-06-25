from flask import Flask, render_template, request, redirect, url_for
import src.matematica as mat
import src.fisica as fis
import src.banco as banco
import json

app = Flask(__name__, template_folder="../templates")

# Dicionários de roteamento de módulos para evitar IFs infinitos
MAPA_MATEMATICA = {
    "aritmetica": (mat.modulo_aritmetica, "Teste de Aritmética"),
    "conjuntos": (mat.modulo_conjuntos, "Teste de Conjuntos Numéricos"),
    "funcao_afim": (mat.modulo_funcoes, "Teste de Função Afim (1º Grau)"),
    "funcao_quadratica": (
        mat.modulo_quadratica,
        "Teste de Função Quadrática (2º Grau)",
    ),
    "inequacoes": (mat.modulo_inequacoes, "Teste de Inequações"),
    "sequencias": (mat.modulo_sequencias, "Teste de Sequências (PA/PG)"),
    "financeira": (mat.modulo_financeira, "Teste de Matemática Financeira"),
    "trigonometria": (mat.modulo_trigonometria, "Teste de Trigonometria"),
}

MAPA_FISICA = {
    "vetores": (fis.modulo_fundamentos_vetores, "Física - Vetores e Grandezas"),
    "cinematica": (fis.modulo_cinematica_mru_mruv, "Física - Cinemática (MRU/MRUV)"),
    "dinamica": (fis.modulo_dinamica_leis_newton, "Física - Dinâmica (Leis de Newton)"),
    "energia": (fis.modulo_trabalho_energia, "Física - Trabalho e Energia"),
    "impulso": (fis.modulo_impulso_colisoes, "Física - Impulso e Colisões"),
    "estatica": (fis.modulo_estatica_gravitacao, "Física - Gravitação e Estática"),
    "hidrostatica": (fis.modulo_hidrostatica_empuxo, "Física - Hidrostática"),
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/gerar", methods=["POST"])
def gerar():
    disciplina = request.form.get("disciplina")
    materia = request.form.get("materia")
    dificuldade = request.form.get("dificuldade")

    # Escolhe o mapa correto baseado na disciplina
    mapa = MAPA_FISICA if disciplina == "fisica" else MAPA_MATEMATICA

    funcao_modulo, titulo = mapa.get(materia, (mat.modulo_aritmetica, "Teste Geral"))

    # Gera as 10 questões dinâmicas
    questoes = funcao_modulo(dificuldade)

    # Prepara o gabarito estruturado para salvar no MySQL
    gabarito = {str(i): q["correta"] for i, q in enumerate(questoes)}
    id_teste = banco.salvar_gabarito(materia, dificuldade, json.dumps(gabarito))

    return render_template(
        "exercicio.html",
        titulo=titulo,
        dificuldade=dificuldade.capitalize(),
        questoes=questoes,
        id_teste=id_teste,
    )


@app.route("/corrigir", methods=["POST"])
def corrigir():
    id_teste = request.form.get("id_teste")
    nome_aluno = request.form.get("nome_aluno")

    gabarito_bruto = banco.buscar_respostas_chave(id_teste)
    if not gabarito_bruto:
        return redirect(url_for("index"))

    gabarito = json.loads(gabarito_bruto)
    acertos = 0
    total = len(gabarito)

    for i in range(total):
        resposta_aluno = request.form.get(f"q{i}")
        if resposta_aluno == gabarito.get(str(i)):
            acertos += 1

    banco.salvar_resultado_aluno(id_teste, nome_aluno, acertos)
    return render_template(
        "resultado.html", nome=nome_aluno, acertos=acertos, total=total
    )


if __name__ == "__main__":
    app.run(debug=True)

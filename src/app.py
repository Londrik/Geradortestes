from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import matematica
import fisica
import banco
import unicodedata

app = Flask(__name__, template_folder="../templates")
app.secret_key = "chave_secreta_para_guardar_questoes"

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

    # --- MAPEAMENTO CORRETO DE CADA MATÉRIA ---
    if materia_opcao == "fundamentos_vetores":
        titulo = "Física - Fundamentos e Vetores"
        questoes = fisica.modulo_fundamentos_vetores(dificuldade=dificuldade)

    elif materia_opcao == "cinematica_mru_mruv":
        titulo = "Física - Cinemática Gráfica (MRU)"
        questoes = fisica.modulo_cinematica_mru_mruv(dificuldade=dificuldade)

    elif materia_opcao == "dinamica_leis_newton":
        titulo = "Física - Dinâmica e Leis de Newton"
        questoes = fisica.modulo_dinamica_leis_newton(dificuldade=dificuldade)

    elif materia_opcao == "trabalho_energia":
        titulo = "Física - Trabalho e Conservação de Energia"
        questoes = fisica.modulo_trabalho_energia(dificuldade=dificuldade)

    elif materia_opcao == "impulso_colisoes":
        titulo = "Física - Impulso e Colisões"
        questoes = fisica.modulo_impulso_colisoes(dificuldade=dificuldade)

    elif materia_opcao == "estatica_gravitacao":
        titulo = "Física - Estática e Gravitação"
        questoes = fisica.modulo_estatica_gravitacao(dificuldade=dificuldade)

    elif materia_opcao == "hidrostatica_empuxo":
        titulo = "Física - Hidrostática e Empuxo"
        questoes = fisica.modulo_hidrostatica_empuxo(dificuldade=dificuldade)
        
    else:
        # Fallback para matemática caso não seja nenhuma das de física
        titulo = "Matemática - Conjuntos Numéricos"
        questoes = matematica.modulo_conjuntos(dificuldade=dificuldade)

    if not questoes:
        return redirect("/")

    session["questoes_atuais"] = questoes
    session["horario_inicio"] = datetime.now().isoformat()

    respostas_chave = "|".join([q["correta"] for q in questoes])
    id_teste = banco.salvar_gabarito(titulo, difficulty_bruta := dificuldade_bruta, respostas_chave)

    return render_template(
        "teste.html", titulo=titulo, questoes=questoes, id_teste=id_teste
    )

@app.route("/corrigir", methods=["POST"])
def corrigir():
    id_teste = request.form.get("id_teste")
    questoes = session.get("questoes_atuais", [])
    horario_inicio_raw = session.get("horario_inicio")
    
    if not questoes or not horario_inicio_raw:
        return "Sessão expirada ou teste não encontrado.", 404
        
    horario_inicio = datetime.fromisoformat(horario_inicio_raw)
    tempo_gasto = (datetime.now() - horario_inicio).total_seconds()
    
    acertos = 0
    html_feedback = ""
    
    for i, q in enumerate(questoes):
        resposta_aluno = request.form.get(f"questao_{i}")
        correta = q["correta"]
        foi_correto = resposta_aluno == correta
        
        if foi_correto:
            acertos += 1
            status_cor = "green"
            status_texto = "✔ Correto"
        else:
            status_cor = "red"
            status_texto = f"✘ Errado (Você marcou: {resposta_aluno})"
            
        resolucao_texto = q.get("resolucao", "Resolução não disponível.")
        tag_imagem = f'<div style="margin: 10px 0;"><img src="{q["imagem"]}" style="max-width:100%; height:auto; border:1px solid #ddd; border-radius:4px;"></div>' if "imagem" in q else ""
        
        html_feedback += f"""
        <div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 15px; border-radius: 5px; text-align: left;">
            <p><strong>Questão {i+1}:</strong> {q['enunciado']}</p>
            {tag_imagem}
            <p style="color: {status_cor}; font-weight: bold;">{status_texto}</p>
            <p style="color: green;"><strong>Resposta correta:</strong> {correta}</p>
            <p style="background-color: #f9f9f9; padding: 10px; border-left: 4px solid #004b87; font-style: italic;">
                <strong>Explicação Física:</strong> {resolucao_texto}
            </p>
        </div>
        """
            
    nota = (acertos / len(questoes)) * 10
    minutos_gastos = int(tempo_gasto // 60)
    segundos_gastos = int(tempo_gasto % 60)
    
    return f"""
    <div style="font-family: Arial, sans-serif; text-align: center; max-width: 800px; margin: 50px auto; padding: 20px;">
        <h2>Resultado da Avaliação (Teste #{id_teste})</h2>
        <p style="color: gray;">Tempo de resolução: {minutos_gastos}m {segundos_gastos}s</p>
        <p style="font-size: 20px;">Você acertou <strong>{acertos}</strong> de <strong>{len(questoes)}</strong> questões.</p>
        <h1 style="color: {'green' if nota >= 6 else 'red'}; font-size: 48px; margin-bottom: 30px;">Nota: {nota:.1f}</h1>
        
        <h3>Revisão das Questões:</h3>
        {html_feedback}
        
        <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #004b87; color: white; text-decoration: none; border-radius: 4px; font-weight: bold;">Voltar ao Início</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)

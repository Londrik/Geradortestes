from flask import Flask, render_template, request, redirect
import matematica
import banco

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    materia_opcao = request.form.get('materia')
    
    if materia_opcao == "1":
        titulo = "Aritmética (Decimais)"
        questoes = matematica.modulo_aritmetica()
    elif materia_opcao == "2":
        titulo = "Introdução às Funções de 1º Grau"
        questoes = matematica.modulo_funcoes()
    else:
        titulo = "Funções Quadráticas (2º Grau)"
        questoes = matematica.modulo_quadratica()
        
    # Converte o gabarito correto em string mapeada (Ex: "0:15;1:22;...")
    gabarito_str = ";".join([f"{i}:{q['correta']}" for i, q in enumerate(questoes)])
    id_teste = banco.salvar_gabarito(titulo, gabarito_str)
    
    return render_template('exercicio.html', titulo=titulo, questoes=questoes, id_teste=id_teste)

@app.route('/corrigir', methods=['POST'])
def corrigir():
    nome_aluno = request.form.get('nome_aluno', 'Aluno Anônimo')
    id_teste = request.form.get('id_teste')
    
    gabarito_bruto = banco.buscar_respostas_chave(id_teste)
    # Transforma "0:15;1:22" em dicionário {0: "15", 1: "22"}
    chaves = dict(item.split(":") for item in gabarito_bruto.split(";"))
    
    acertos = 0
    total_questoes = len(chaves)
    
    for i in range(total_questoes):
        resposta_aluno = request.form.get(f"q{i}")
        if resposta_aluno == chaves.get(str(i)):
            acertos += 1
            
    banco.salvar_resultado_aluno(id_teste, nome_aluno, acertos)
    
    return render_template('resultado.html', nome=nome_aluno, acertos=acertos, total=total_questoes)

if __name__ == '__main__':
    app.run(debug=True)
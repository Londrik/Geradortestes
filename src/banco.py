import mysql.connector

def obter_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # Coloque sua senha do MySQL aqui se houver
        database="gerador_matematica"
    )

def salvar_gabarito(materia, respostas_chave):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO gabaritos (materia, respostas_chave) VALUES (%s, %s)"
    cursor.execute(comando, (materia, respostas_chave))
    id_teste = cursor.lastrowid
    conexao.commit()
    cursor.close()
    conexao.close()
    return id_teste

def buscar_respostas_chave(id_teste):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    comando = "SELECT respostas_chave FROM gabaritos WHERE id_teste = %s"
    cursor.execute(comando, (id_teste,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado[0] if resultado else ""

def salvar_resultado_aluno(id_teste, nome_aluno, acertos):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO resultados_alunos (id_teste, nome_aluno, acertos) VALUES (%s, %s, %s)"
    cursor.execute(comando, (id_teste, nome_aluno, acertos))
    conexao.commit()
    cursor.close()
    conexao.close()
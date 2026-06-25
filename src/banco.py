import os
import mysql.connector


def obter_conexao():
    # O os.getenv("VARIAVEL", "PADRAO") lê o Docker, se não achar usa o padrão
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),  # Usa a senha do Docker ou vazia local
        database=os.getenv("DB_NAME", "gerador_matematica"),
        port=int(
            os.getenv("DB_PORT", "3306")
        ),  # Internamente no Docker a porta do banco é sempre 3306
    )


def inicializar_banco():
    """Cria as tabelas automaticamente caso elas não existam no banco."""
    conexao = obter_conexao()
    cursor = conexao.cursor()

    # Criação da tabela gabaritos incluindo a coluna de dificuldade
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gabaritos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            materia VARCHAR(255) NOT NULL,
            dificuldade VARCHAR(50) DEFAULT 'intermediario',
            respostas_chave TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Executa um ALTER TABLE seguro caso a coluna 'dificuldade' não exista em containers antigos
    try:
        cursor.execute(
            "ALTER TABLE gabaritos ADD COLUMN dificuldade VARCHAR(50) DEFAULT 'intermediario'"
        )
    except mysql.connector.errors.ProgrammingError:
        # Se a coluna já existir, ignora o erro silenciosamente
        pass

    # Criação da tabela resultados_alunos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados_alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_teste INT NOT NULL,
            nome_aluno VARCHAR(255) NOT NULL,
            acertos INT NOT NULL,
            data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_teste) REFERENCES gabaritos(id) ON DELETE CASCADE
        )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()


def salvar_gabarito(materia, dificuldade, respostas_chave):
    """Salva o gabarito associando a matéria e a respectiva dificuldade escolhida."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO gabaritos (materia, dificuldade, respostas_chave) VALUES (%s, %s, %s)"
    cursor.execute(comando, (materia, dificuldade, respostas_chave))
    id_teste = cursor.lastrowid
    conexao.commit()
    cursor.close()
    conexao.close()
    return id_teste


def buscar_respostas_chave(id_teste):
    conexao = obter_conexao()
    cursor = conexao.cursor()

    # CORREÇÃO DEFINITIVA: Tabela certa (gabaritos) e Coluna certa (id)
    comando = "SELECT respostas_chave FROM gabaritos WHERE id = %s"

    cursor.execute(comando, (id_teste,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return resultado[0]  # Retorna a string das respostas (gabarito)
    return None


def salvar_resultado_aluno(id_teste, nome_aluno, acertos):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    comando = "INSERT INTO resultados_alunos (id_teste, nome_aluno, acertos) VALUES (%s, %s, %s)"
    cursor.execute(comando, (id_teste, nome_aluno, acertos))
    conexao.commit()
    cursor.close()
    conexao.close()


# Executa a criação das tabelas assim que o módulo for importado pelo Flask
try:
    inicializar_banco()
except Exception as e:
    print(
        f"Aviso: Não foi possível inicializar as tabelas (o banco pode estar subindo): {e}"
    )

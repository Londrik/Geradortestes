import sqlite3

def conectar():
    conn = sqlite3.connect("banco.db")
    return conn, conn.cursor()

def criar_tabelas():
    conn, cursor = conectar()
    # CORREÇÃO: Alterado 'NOT EXISTS' para 'NOT NULL' na sintaxe do SQL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gabaritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            materia TEXT NOT NULL,
            dificuldade TEXT,
            respostas TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def salvar_gabarito(materia, dificuldade, respostas_chave):
    conn, cursor = conectar()
    comando = "INSERT INTO gabaritos (materia, dificuldade, respostas) VALUES (?, ?, ?)"
    cursor.execute(comando, (materia, dificuldade, respostas_chave))
    id_teste = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_teste

import sqlite3

def conectar():
    conn = sqlite3.connect("banco.db")
    return conn, conn.cursor()

def criar_tabelas():
    conn, cursor = conectar()
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
    cursor.execute("INSERT INTO gabaritos (materia, dificuldade, respostas) VALUES (?, ?, ?)", (materia, dificuldade, respostas_chave))
    id_teste = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_teste

def buscar_gabarito(id_teste):
    conn, cursor = conectar()
    cursor.execute("SELECT respostas FROM gabaritos WHERE id = ?", (id_teste,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

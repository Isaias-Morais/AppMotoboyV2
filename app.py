
from BancoDeDados.dia_de_trabalho_repositorio import *
from servicos.add_dia_de_trabalho import registra_dia_de_trabalho
from BancoDeDados.init_db import criar_tabelas

import sqlite3
criar_tabelas()

conn = get_conexao()
curso = conn.cursor()
curso.execute("""
SELECT
    motoboy.nome,
    moto.modelo,
    manutencao.tipo
FROM motoboy
LEFT JOIN moto ON moto.motoboy_id = motoboy.id
LEFT JOIN manutencao ON manutenca.moto_id = moto.id;

""")

print("Motoboy | Moto | Litros | Valor | Data")
print("-" * 50)

resultados = curso.fetchall()

for linha in resultados:
    print(linha)

conn.close()



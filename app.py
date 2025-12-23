
from BancoDeDados.abastecimento_repositorio import *
from servicos.add_abastecimento import registra_abastecimento
from BancoDeDados.moto_repositorio import listar_moto

import sqlite3
registra_abastecimento(None,'shell',10,60,True,17000,1)
listar_abastecimento()
listar_moto()

conn = get_conexao()
curso = conn.cursor()
curso.execute("""
        SELECT
            motoboy.nome,
            moto.modelo,
            abastecimento.litros,
            abastecimento.valor
        FROM motoboy
        JOIN moto ON moto.motoboy_id = motoboy.id
        JOIN abastecimento ON abastecimento.moto_id = moto.id
""")

print("Motoboy | Moto | Litros | Valor | Data")
print("-" * 50)

resultados = curso.fetchall()

for linha in resultados:
    print(linha)

conn.close()

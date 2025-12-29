from BancoDeDados.conexao import get_conexao
def buscar_dia_de_trabalho():
    pass

def busca_abastecimento(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
        SELECT
            a.data_abastecimento,
            a.valor,
            a.litros,
            a.valor_litro,
            a.quilometragem
        FROM abastecimento a
        JOIN moto m ON m.id = a.moto_id
        WHERE m.id = ?
            AND a.data_abastecimento >= date('now','-30 days')
            AND a.data_abastecimento <= date('now')
        ORDER BY a.data_abastecimento;
        '''
    cursor.execute(sql,(moto_id,))
    resultado = cursor.fetchall()

    return resultado

def busca_manutencoes():
    pass

def busca_moto():
    pass


busca_abastecimento(1)
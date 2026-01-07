from BancoDeDados.conexao import get_conexao


def historico_dias(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
    SELECT 
        d.data_trabalhada,
        d.quilometragem_final - d.quilometragem_inicial,
        d.ganho_bruto
    FROM dia_de_trabalho d
        WHERE d.moto_id = ?
    ORDER BY d.data_trabalhada ASC
    '''
    cursor.execute(sql,(moto_id,))
    dados = cursor.fetchall()
    conn.close()

    return dados

def historico_manutencoes(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
    SELECT
        m.data_manutencao,
        m.tipo,
        m.descricao,
        m.valor,
        m.quilometragem
    FROM manutencao m
        WHERE m.moto_id = ?
    ORDER BY m.data_manutencao ASC
          '''
    cursor.execute(sql,(moto_id,))
    dados = cursor.fetchall()
    conn.close()

    return dados


def historicos_abastecimentos(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
          SELECT a.data_abastecimento,
                 a.posto,
                 a.litros,
                 a.valor,
                 a.tanque_completo,
                 a.quilometragem
          FROM abastecimento a
          WHERE a.moto_id = ?
          ORDER BY a.data_abastecimento ASC
          '''
    cursor.execute(sql, (moto_id,))
    dados = cursor.fetchall()
    conn.close()

    return dados


from BancoDeDados.conexao import get_conexao

def buscar_dia_de_trabalho(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
        SELECT
            d.ganho_bruto AS ganho,
            d.quilometragem_final - d.quilometragem_inicial AS km
        FROM dias_de_trabalho d
        JOIN moto m ON m.id = d.moto_id
        WHERE m.id = ?
            and d.data_trabalhada = date('now','localtime')
    '''
    cursor.execute(sql,(moto_id,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado is None:
        return {
            'ganho':0.0,
            'km_dia':0.0
        }
    ganho,km = resultado

    return {
        'ganho':ganho,
        'km_dia':km
    }

def busca_abastecimento(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
        SELECT
            SUM(a.valor) AS valor,
            SUM(a.litros) AS litros,
            MAX(a.quilometragem) - MIN(a.quilometragem) AS km
        FROM abastecimento a
        JOIN moto m ON m.id = a.moto_id
        WHERE m.id = ?
        AND a.data_abastecimento >= date('now','-30 days')
        AND a.data_abastecimento <= date('now')
        '''
    cursor.execute(sql,(moto_id,))
    valor,litros,km = cursor.fetchone()
    conn.close()
    return {
        'valor_abastecimento':valor,
        'litros':litros,
        'km_abastecimento': km
    }

def busca_manutencoes(moto_id):
    conn = get_conexao()
    curso = conn.cursor()
    sql = ''' 
        SELECT
            SUM(m.valor) AS valor,
            MAX(m.quilometragem) - MIN(m.quilometragem) AS km
        FROM manutencao m 
        JOIN moto mo ON mo.id = m.moto_id
        WHERE mo.id = ?
        AND m.data_manutencao >= date('now','-30 days')
        AND m.data_manutencao <= date('now')
    '''
    curso.execute(sql,(moto_id,))
    valor,km = curso.fetchone()
    conn.close()
    return {
        'valor_manutencao':valor,
        'km_manutencao':km
    }

def busca_abastecimento_consumo_medio(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
        SELECT 
            a.quilometragem AS km,
            a.litros AS litros
        FROM abastecimento a
        JOIN moto m ON m.id = a.moto_id
        WHERE m.id = ?
            AND a.tanque_completo = 1
        ORDER BY a.quilometragem DESC
        LIMIT 10
    '''

    cursor.execute(sql, (moto_id,))
    dados = cursor.fetchall()
    conn.close()

    return dados



def busca_consumo_moto(moto_id):
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
        SELECT
            mo.cosumo AS consumo
        FROM moto mo
        JOIN moto m ON m.id = m.id
        WHERE m.id =?
    '''

    cursor.execute(sql,(moto_id,))
    consumo = cursor.fetchone()
    conn.close()

    return consumo

print(busca_consumo_moto(1))
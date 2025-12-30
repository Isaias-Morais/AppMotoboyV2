
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
        'valor':valor,
        'litros':litros,
        'km_mes': km
    }




def busca_manutencoes():
    pass

def busca_moto():
    pass


i = busca_abastecimento(1)
print(i)
a = buscar_dia_de_trabalho(1)
print(a)
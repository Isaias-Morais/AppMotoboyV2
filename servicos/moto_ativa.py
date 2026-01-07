from BancoDeDados.conexao import get_conexao
from validacoes.moto_exitente import moto_existe


def busca_moto_ativa():
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            m.moto_ativa_id AS id
        FROM motoboy m 
        WHERE m.id = 1
    ''')

    id = cursor.fetchone()
    conn.close()

    return id[0] if id and id[0] is not None else None


def definir_moto_ativa(moto_id):
    if not moto_existe(moto_id):
        return False,'moto não existe'
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
            UPDATE motoboy 
            SET moto_ativa_id = ?
            WHERE id = 1
        '''
    cursor.execute(sql,(moto_id,))

    conn.commit()
    conn.close()

def redefinir_moto_ativa():
    conn = get_conexao()
    cursor = conn.cursor()
    sql = '''
        UPDATE motoboy
        SET moto_ativa_id = NULL
        WHERE id = 1
    '''
    cursor.execute(sql)

redefinir_moto_ativa()
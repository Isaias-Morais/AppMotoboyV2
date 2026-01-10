from BancoDeDados.conexao import get_conexao
from validacoes.moto_exitente import moto_existe

def salvar_moto(moto):
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            INSERT INTO moto(
                marca,
                modelo,
                ano,
                quilometragem,
                cosumo,
                motoboy_id
            )
            values (?,?,?,?,?,?)
        ''',(moto._marca,
             moto._modelo,
             moto._ano,
             moto._quilometragem_total,
             moto._consumo,
             moto._motoboy
             )
    )
    moto.id = curso.lastrowid

    conn.commit()
    conn.close()

def listar_moto():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            SELECT * FROM moto
        """
    )
    moto = curso.fetchall()

    for moto in moto:
        print(moto)

    conn.close()

def excluir_moto(moto_id):
    conn = get_conexao()
    curso = conn.cursor()

    sql = '''
          DELETE 
          FROM moto
          WHERE id = ? 
          '''

    curso.execute(sql, (moto_id,))

    conn.commit()
    conn.close()


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


from BancoDeDados.conexao import get_conexao
from validacoes.moto_exitente import moto_existe


def atualizar_consumo(moto_id=0,consumo=0):
    if not moto_existe(moto_id):
        return False, 'moto não existe'

    if not isinstance(consumo,(int)) or consumo <= 0 :
        return False, 'consumo invalido'

    conn = get_conexao()
    cursor = conn.cursor()

    sql = '''
          UPDATE moto
          SET cosumo = ?
          WHERE id = ? 
          '''

    cursor.execute(sql,(consumo,moto_id))
    conn.commit()
    conn.close()

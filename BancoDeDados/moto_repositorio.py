from BancoDeDados.conexao import get_conexao

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
    pass
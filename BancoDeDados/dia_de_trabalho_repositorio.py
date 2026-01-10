from BancoDeDados.conexao import get_conexao
def salvar_dia_de_trabalho(dia_de_trabalho):
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            INSERT INTO dia_de_trabalho(
                moto_id,
                data_trabalhada,
                quilometragem_inicial,
                quilometragem_final,
                ganho_bruto
            )        
            VALUES(?,?,?,?,?)
        ''',
        (
            dia_de_trabalho._moto_id,
            dia_de_trabalho._data,
            dia_de_trabalho._km_inicial,
            dia_de_trabalho._km_final,
            dia_de_trabalho._ganho_bruto,

        )
    )
    dia_de_trabalho.id = curso.lastrowid
    conn.commit()
    conn.close()

def listar_dia_de_trabalho():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            SELECT * FROM dia_de_trabalho
        """
    )
    dias = curso.fetchall()

    for dia in dias:
        print(dia)


def excluir_dias_trabalhados(moto_id):
    conn = get_conexao()
    curso = conn.cursor()

    sql = '''
          DELETE 
          FROM dia_de_trabalho
          WHERE moto_id = ? 
          '''

    curso.execute(sql, (moto_id,))

    conn.commit()
    conn.close()


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

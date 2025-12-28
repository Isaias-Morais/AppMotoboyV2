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
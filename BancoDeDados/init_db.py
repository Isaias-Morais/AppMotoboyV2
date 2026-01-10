from BancoDeDados.conexao import get_conexao
def criar_tabelas():
    criar_tabela_motoboy()
    criar_tabela_motos()
    criar_tabela_abatecimento()
    criar_tabela_manutencao()
    criar_tabela_dia_de_trabalho()

def criar_tabela_motoboy():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            CREATE TABLE IF NOT EXISTS motoboy(
            id INTEGER PRIMARY KEY ,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL,
            moto_ativa_id INTEGER 
            )
        '''
        )
    conn.commit()
    conn.close()


def criar_tabela_motos():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            CREATE TABLE IF NOT EXISTS moto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            quilometragem INTEGER NOT NULL,
            cosumo REAL NOT NULL,
            motoboy_id INTEGER NOT NULL,
            FOREIGN KEY (motoboy_id) REFERENCES motoboy(id)
            )
        """
        )
    conn.commit()
    conn.close()


def criar_tabela_abatecimento():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        """
            CREATE TABLE IF NOT EXISTS abastecimento(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moto_id INTEGER NOT NULL,
            data_abastecimento DATA,
            posto TEXT NOT NULL,
            valor REAL NOT NULL,
            litros REAL NOT NULL,
            valor_litro REAL NOT NULL,
            tanque_completo BOOLEAN NOT NULL,
            quilometragem INTEGER NOT NULL,
            FOREIGN KEY (moto_id) references moto(id)
        )
        """

        )
    conn.commit()
    conn.close()

def criar_tabela_manutencao():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            CREATE TABLE IF NOT EXISTS manutencao(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moto_id INTEGER NOT NULL,
            data_manutencao DATA,
            tipo TEXT NOT NULL,
            descricao TEXT,
            valor REAL NOT NULL,
            quilometragem INTEGER NOT NULL,
            FOREIGN KEY (moto_id) references moto(id)
            )
        '''
        )
    conn.commit()
    conn.close()

def criar_tabela_dia_de_trabalho():
    conn = get_conexao()
    curso = get_conexao()
    curso.execute(
        '''
            CREATE TABLE IF NOT EXISTS dia_de_trabalho(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moto_id INTEGER NOT NULL,
            data_trabalhada DATA,
            quilometragem_inicial INTEGER NOT NULL,
            quilometragem_final INTEGER NOT NULL,
            ganho_bruto REAL NOT NULL,
            FOREIGN KEY (moto_id) references moto(id)
            )     
        '''
    )
    conn.commit()
    conn.close()
from BancoDeDados.conexao import get_conexao
def criar_tabelas():
    criar_tabela_motoboy()

def criar_tabela_motoboy():
    conn = get_conexao()
    curso = conn.cursor()
    curso.execute(
        '''
            CREATE TABLE IF NOT EXISTS motoboy(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL
            )
        '''
    )

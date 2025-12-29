from BancoDeDados.abastecimento_repositorio import  *
from servicos.add_abastecimento import registra_abastecimento
from BancoDeDados.dia_de_trabalho_repositorio import *
from servicos.add_dia_de_trabalho import registra_dia_de_trabalho
from BancoDeDados.init_db import criar_tabelas

import sqlite3

registra_abastecimento(1,12,2025,'ipiranga',10,6,True,1000,1)
listar_abastecimento()
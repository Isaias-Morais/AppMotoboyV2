from servicos.add_motoboy import registrar_motoboy
from BancoDeDados.init_db import criar_tabelas
from BancoDeDados.motoboy_repositorio import *
criar_tabelas()
registrar_motoboy('julio',18,'isaiasmoraisdelima@gmail.com')
listar_motoboy()

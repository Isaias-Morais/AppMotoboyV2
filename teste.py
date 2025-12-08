from modelos.moto import Moto
moto1 = Moto('Cg 160',"preta",0)
moto1.RegistraManutencao('oleo',40,1000)
moto1.RegistraAbastecimento(60,10,True)
print(moto1.manutencoes)
print(moto1.abastecimento)
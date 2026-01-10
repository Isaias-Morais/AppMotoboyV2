from BancoDeDados.abastecimento_repositorio import listar_abastecimento
from BancoDeDados.conexao import *
from BancoDeDados.dia_de_trabalho_repositorio import listar_dia_de_trabalho
from BancoDeDados.init_db import *
from BancoDeDados.manutecao_repositorio import listar_manutencao
from BancoDeDados.moto_repositorio import *
from servicos.add_abastecimento import *
from servicos.add_manutecao import registra_manutencao
from servicos.add_moto import *
from servicos.add_dia_de_trabalho import *
from servicos.add_motoboy import *
from servicos.exluir_moto import excluir_moto_geral
from servicos.resumo_dia_service import *
from validacoes.motoboy_existe import *
from interface.utilidades import *

get_conexao()
criar_tabelas()
cabecalho("APP_MOTOBOY",55)
cabecalho("RESUMO DO DIA",55)
moto = busca_moto_ativa()
resumo = resumo_dia()
print(f'moto ativa - {moto}')
for chave, valor in resumo.items():
    print(f'{chave:<26} : {valor:>26}')

while True:

    if not  motoboy_existe():
        print('Adicione seus dados para continuarmos')
        nome  = (input("Nome : "))
        idade = leiaint('Idade')
        email = (input('Email : '))
        print(registrar_motoboy(nome,idade,email))


    resposta_menu = menu("MENU",['MOTO','DIA_TRABALHADO','ABASTECIMENTO/MANUTENÇAO','HISTORICO','SAIR'],55)

    match resposta_menu:
        case 1:
            cabecalho('MOTO', 55)
            while True:
                resposta_moto_menu = menu('MOTO', ['REGISTRA MOTO',"ATIVA MOTO","EXCLUIR MOTO",'VOLTAR'])
                match resposta_moto_menu:
                    case 1:
                            marca = input('Qual e a marca de sua moto?')
                            modelo = input('Qual o modelo de sua moto?')
                            ano = leiaint('Qual o ano de sua moto?')
                            quilometragem = leiaint('Qual a quilometragem de sua moto?')
                            consumo = leiaint("Qual consumo medio de sua moto?")
                            print(registra_moto(marca,modelo,ano,quilometragem,consumo))

                    case 2:
                        listar_moto()
                        id = leiaint('ID : ')
                        print(definir_moto_ativa(id))

                    case 3:
                        listar_moto()
                        id = leiaint('ID : ')
                        excluir_moto_geral(id)

                    case 4:
                        break

                    case _:
                        print('digite um opcao valida ')
                        continue

        case 2:
            cabecalho('DIA DE TRABALHO',55)
            resp = sim_ou_nao('Quer definir uma data especifica')
            if not resp:
                dia = None
                mes = None
                ano = None
            else:
                dia = leiaint("DIA : ")
                mes = leiaint("MES : ")
                ano = leiaint('ANO : ')

            km_inicial = leiaint('Quilometragem inicial : ')
            km_final = leiaint("Quilometragem final : ")
            ganho_bruto = leiafloat("Faturamento bruto :  ")
            listar_moto()
            moto_id = leiaint('ID : ')

            print(registra_dia_de_trabalho(dia,mes,ano,km_inicial,km_final,ganho_bruto,moto_id))

        case 3:
            while True:
                resposta_menu_abasmanu = menu('ABASTECIMENTO/MANUTENÇÕES',['ABASTECIMENTO','MANUTENÇÕES',"VOLTAR"], 55)
                match resposta_menu_abasmanu:
                    case 1 :
                        cabecalho('ABASTECIMENTO', 55)
                        resp = sim_ou_nao('Quer definir uma data especifica')
                        if not resp:
                            dia = None
                            mes = None
                            ano = None
                        else:
                            dia = leiaint("DIA : ")
                            mes = leiaint("MES : ")
                            ano = leiaint('ANO : ')
                        posto = input("Local do abastecimento : ")
                        litros = leiafloat('Litros/L : ')
                        valor = leiafloat('Valor R$ : ')
                        tanque_completo = sim_ou_nao('Tanque cheio : ')
                        quilometragem_abastecimento = leiaint('KM do abastecimento')
                        listar_moto()
                        moto_id = leiaint('ID : ')
                        print(registra_abastecimento(dia,mes,ano,posto,litros,valor,tanque_completo,quilometragem_abastecimento,moto_id))

                    case 2:
                        cabecalho('MANUTENÇÃO', 55)
                        resp = sim_ou_nao('Quer definir uma data especifica')
                        if not resp:
                            dia = None
                            mes = None
                            ano = None
                        else:
                            dia = leiaint("DIA : ")
                            mes = leiaint("MES : ")
                            ano = leiaint('ANO : ')
                        tipo = input('Tipo de manuteção : ')
                        descricao = input('Descricao : ')
                        valor = leiafloat('Valor : ')
                        quilometragem_manutencao = leiaint('KM da Manutenção : ')
                        listar_moto()
                        moto_id = leiaint('ID : ')
                        print(registra_manutencao(dia, mes, ano, tipo, descricao, valor, quilometragem_manutencao, moto_id))
                    case 3:
                        break

                    case _:
                        print('digite um opcao valida ')
                        continue


        case 4 :
            resp_historico = menu('HISTORICO',['Dia',"Abastecimenos" , 'Manutenção'],55)

            match resp_historico:
                case 1:
                    listar_dia_de_trabalho()
                case 2:
                    listar_abastecimento()
                case 3:
                    listar_manutencao()

        case 5:
            break

        case _:
            print('digite um opcao valida ')
            continue
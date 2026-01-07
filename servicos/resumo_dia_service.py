from servicos.moto_ativa import *
from BancoDeDados.finaceiro_repositorio import *
from servicos.calculos import *

def resumo_dia():
    moto_id = busca_moto_ativa()
    dia_de_trabalho  = buscar_dia_de_trabalho(moto_id) or {}
    abastecimento_geral = busca_abastecimento(moto_id) or {}
    manutencoes = busca_manutencoes(moto_id) or {}
    consumo = busca_consumo_moto(moto_id) or 0


    valor_do_dia = dia_de_trabalho.get('ganho',0)
    km_dia = dia_de_trabalho.get('km_dia',0)

    valor_manutencao = manutencoes.get('valor_manutencao',0 )
    km_manutencao = manutencoes.get('km_manutencao',0)

    valor_abastecimento = abastecimento_geral.get('valor_abastecimento',0)
    km_abastecimeto = abastecimento_geral.get('km_abastecimento',0)
    litros_abastecimento = abastecimento_geral.get('litros',0)


    preco_gasolina = calcular_preco_medio_combustivel(valor_abastecimento,litros_abastecimento)
    custo_manutencao = calcular_custo_manutecao_km(valor_manutencao,km_manutencao)
    custo_combustivel = calcular_custo_combustivel_km(valor_abastecimento,km_abastecimeto)
    custo_total = calcular_custo_total_km(custo_combustivel,custo_manutencao)
    liquido = calcular_lucro_liquido(valor_do_dia,km_dia,custo_total)

    resumo_dia = {
        'bruto':valor_do_dia,
        'km':km_dia,
        'preco_gasolina':preco_gasolina,
        'custo_combustivel_km':custo_combustivel,
        'custo_manutencao_km':custo_manutencao,
        'custo_km_total':custo_total,
        'consumo_medio': consumo,
        'lucro':liquido
    }
    return resumo_dia

print(resumo_dia())
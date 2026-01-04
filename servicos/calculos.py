def calcular_preco_medio_combustivel(valor,litros ):

def calcular_custo_manutecao_km():

def calcular_custo_total_km():

def calcular_lucro_liquido():

def calcular_consumo_medio_real(km_rodados):
    km_total = 0
    litros_total = 0
    historico = km_rodados

    for i in historico:
        km_total += i[0]
        litros_total += i[1]

    consumo_medio = km_total / litros_total

    return consumo_medio

def calcular_km_rodados(abastecimentos_cheios):

    abastecimento = abastecimentos_cheios
    resultado = []

    for i in range(1,len(abastecimento)):
        km_atual = abastecimento[i][0]
        km_anterios = abastecimento [i-1][0]

        km_rodados = km_atual - km_anterior
        litros = abastecimento[i][1]

        if km_rodados >0 and litros >0:
            resultado.append((km_rodados,litros))

    return resultado


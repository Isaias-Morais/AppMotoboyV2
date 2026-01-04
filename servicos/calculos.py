def calcular_preco_medio_combustivel(valor=0,litros=0 ):
    if valor <0 or litros < 0:
        return False, 'parametro invalido'

    preco_litro = valor/litros

    return preco_litro

def calcular_custo_manutecao_km(valor=0,km_rodados=0):
    if valor <0 or km_rodados <= 0:
        return False, 'parametro invalido'

    custo_manutencao = valor/km_rodados

    return custo_manutencao

def calcular_custo_combustivel_km(valor,km_rodados):
    if valor <0 or km_rodados < 0:
        return False, 'parametro invalido'

    custo_combustivel = valor/km_rodados

    return custo_combustivel

def calcular_custo_total_km(valor1,valor2):
    if valor1 < 0 or valor2 < 0:
        return False, 'parametro invalido'

    custo_km = valor1+valor2
    return custo_km


def calcular_lucro_liquido(bruto,km_rodados,custo_km):
    if bruto <0 or km_rodados <0 or custo_km <0:
        return False, 'parametro invalido'

    custo_total = custo_km*km_rodados
    liquido = bruto - custo_total

    return liquido

def calcular_consumo_medio_real(historico):
    km_total = 0
    litros_total = 0
    historico = historico

    for i in historico:
        km_total += i[0]
        litros_total += i[1]

    consumo_medio = km_total / litros_total

    return consumo_medio

def calcular_km_rodados(abastecimentos_cheios=None):

    abastecimento = abastecimentos_cheios
    resultado = []

    for i in range(1,len(abastecimento)):
        km_atual = abastecimento[i][0]
        km_anterior = abastecimento [i-1][0]

        km_rodados = km_atual - km_anterior
        litros = abastecimento[i][1]

        if km_rodados >0 and litros >0:
            resultado.append((km_rodados,litros))

    return resultado


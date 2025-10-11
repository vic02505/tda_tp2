def planear_estrategia(soldados, ataques):
    opt = [0] * (len(soldados) + 1)
    for i in range(1, len(soldados) + 1):
        #Atacar probando todas las cargas de energia
        for carga in range(1, i + 1):
            ultimo_ataque = i - carga
            rafaga_actual = soldados[i-1]
            ataque_actual = ataques[carga-1]

            opt[i] = max(opt[i], opt[ultimo_ataque] + min(rafaga_actual, ataque_actual))

    return opt[-1], reconstruccion(opt, soldados, ataques)


#ec de recurrencia
# opt[i] = max(opt[i-carga] +  min(soldados[i-1], ataques[carga-1]) )

# carga = minutos de energia cargados
# max representa el maximo de bajas posibles probando con todos los minutos de cargas posibles


def reconstruccion(opt, soldados, ataques):
    estrategia = [''] * len(soldados)
    i = len(soldados)
    while i > 0:
        for carga in range(1, i+1):
            ultimo_ataque = i - carga
            rafaga_actual = soldados[i-1]
            ataque_actual = ataques[carga-1]

            if opt[i] == opt[ultimo_ataque] + min(rafaga_actual, ataque_actual):
                estrategia[i-1] = 'Atacar'
                i = i - carga
                break
            estrategia[ultimo_ataque-1] = 'Cargar'
    return estrategia

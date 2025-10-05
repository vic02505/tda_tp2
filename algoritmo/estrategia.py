def planear_estrategia(soldados, ataques):
    opt = [0] * (len(soldados) + 1)
    for i in range(1, len(soldados) + 1):
        #opcion 1 no atacar
        opt[i] = opt[i-1]# creo que esto nunca es solucion
        #opcion 2 atacar probando todas las cargas de energia
        for carga in range(1, i + 1):
            ultimo_ataque = i - carga
            rafaga_actual = soldados[i-1]
            ataque_actual = ataques[carga-1]

            opt[i] = max(opt[i], opt[ultimo_ataque] + min(rafaga_actual, ataque_actual))

    return opt[-1], reconstruccion(opt, soldados, ataques)


#ec de recurrencia
# opt[i] = max(opt[i-1], max(opt[i-carga] + min(soldados[i-1], ataques[carga-1])))

# carga = minutos de energia cargados
# el segundo max representa el maximo de bajas posibles probando con todos los minutos de cargas posibles


def reconstruccion(opt, soldados, ataques):
    estrategia = [''] * len(soldados)
    i = len(soldados)
    while i > 0:
        if opt[i] == opt[i-1]:# creo que esto nunca pasa
            estrategia[i-1]= 'Cargar'
            i -= 1
        else:
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


if __name__ == "__main__":
    # correr_pruebas_con_estrategia()
    soldados = [995, 132, 886, 525, 546, 991, 929, 923, 235, 345, 314, 852, 913, 632, 616, 987, 216, 721, 813, 591, 573, 396, 149, 235, 421, 942, 613, 852, 605, 865, 297, 489, 695, 423, 302, 482, 116, 624, 426, 232, 581, 733, 800, 171, 730, 106, 828, 215, 545, 764]
    ataques = [5, 16, 239, 320, 330, 356, 392, 408, 466, 646, 780, 782, 854, 889, 915, 929, 935, 969, 977, 1002, 1013, 1070, 1212, 1254, 1281, 1498, 1625, 1811, 1953, 2061, 2072, 2087, 2466, 2505, 2741, 2751, 2770, 2808, 2853, 2937, 3088, 3146, 3294, 3319, 3345, 3374, 3471, 3550, 3742, 3923]
            
    cantidad, estrategia = planear_estrategia(soldados, ataques)
    print(f"Estrategia: {estrategia}")
    print(f"Cantidad de bajas: {cantidad}")
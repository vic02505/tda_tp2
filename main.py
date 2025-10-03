
def main(soldados, ataques):
    opt = [0] * len(soldados)
    opt[0] = min(soldados[0], ataques[0])
    opt[1] = max((opt[0] + min(soldados[1], ataques[0])), min(soldados[1], ataques[1]))

    for i in range(2, len(soldados)):
        k = indice_ataque(ataques, soldados[i], i)+1
        maximas_bajas = min(soldados[i], ataques[k-1])
        if k > i:
            opt[i] = max((maximas_bajas), (opt[i-1] + min(soldados[i], ataques[0])))
        else:
            opt[i] = max((opt[i-k] + maximas_bajas), (opt[i-1] + min(soldados[i], ataques[0])))
    return opt[-1]


def indice_ataque(ataques, n_soldados, i_actual):
    for i in range(i_actual):
        if ataques[i] >= n_soldados:
            return i
    return i_actual
    


if __name__ == "__main__":
    soldados = [271, 533, 916, 656, 664]
    ataques = [21, 671, 749, 833, 1543]
    
    print(main(soldados, ataques))

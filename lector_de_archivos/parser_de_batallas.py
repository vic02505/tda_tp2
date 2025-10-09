def leer_batalla_txt(path_del_archivo: str):
    """
    Lee un archivo
    - 1ra línea: n
    - siguientes n líneas: soldados
    - siguientes n líneas: ataques
    Devuelve: (soldados, ataques)
    """
    with open(path_del_archivo, "r") as f:
        lineas = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    n = int(lineas[0])
    soldados = [int(x) for x in lineas[1:1+n]]
    ataques = [int(x) for x in lineas[1+n:1+2*n]]
    return soldados, ataques
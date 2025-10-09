def obtener_resultados_esperados(path_de_archivo_de_resultados: str) -> dict:
    """
    Lee un archivo de resultados esperados estilo:
    nombre.txt
    Cantidad de tropas eliminadas: 1234
    """
    resultados_esperados = {}
    with open(path_de_archivo_de_resultados, "r") as f:
        lineas = [line.strip() for line in f if line.strip()]
    for i in range(len(lineas)):
        if lineas[i].endswith('.txt'):
            nombre = lineas[i]
            # Buscar la línea con "Cantidad de tropas eliminadas:"
            for j in range(i+1, min(i+5, len(lineas))):
                if "Cantidad de tropas eliminadas:" in lineas[j]:
                    valor = int(lineas[j].split(":")[1].strip())
                    resultados_esperados[nombre] = valor
                    break
    return resultados_esperados

def obtener_estrategias_esperadas(path_de_archivo_de_resultados: str) -> dict:
    """
    Devuelve un diccionario {nombre.txt: [lista de acciones]}
    """
    estrategias = {}
    with open(path_de_archivo_de_resultados, "r") as f:
        lineas = [line.strip() for line in f if line.strip()]
    i = 0
    while i < len(lineas):
        if lineas[i].endswith('.txt'):
            nombre = lineas[i]
            estrategia = []
            # Buscar la línea de estrategia
            for j in range(i+1, min(i+6, len(lineas))):
                if lineas[j].startswith("Estrategia:"):
                    # Extraer acciones
                    acciones = [x.strip() for x in lineas[j].split(":")[1].split(",")]
                    estrategia = acciones
                    break
            estrategias[nombre] = estrategia
        i += 1
    return estrategias
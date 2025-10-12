
def imprimir_estrategia(enemigos_liquidados, ataques, nombre_archivo):
    print("----------------------------------------------------------------")
    print(f"Estrategia para: {nombre_archivo}\n")
    print(f"Enemigos liquidados: {enemigos_liquidados}\n")

    print(f"Acciones:")
    for i, accion in enumerate(ataques, start=1):
        print(f"{i}. {accion}")
    print("----------------------------------------------------------------")
from algoritmo.estrategia import planear_estrategia
from lector_de_archivos.parser_de_batallas import leer_batalla_txt
from printer.printer import imprimir_estrategia
from pruebas import correr_pruebas_sobre_estrategias
#from utils.graficos import generar_grafico
import sys

ARCHIVOS_CATEDRA = "1"
PRUEBAS_ARCHIVOS_CATEDRA = "2"
ARCHIVOS_PROPIOS = "3"
PRUEBAS_ARCHIVOS_PROPIOS = "4"
GENERAR_GRAFICO = "5"

def correr_algoritmo(modo_de_ejecucion, nombre_archivo):
    path_base = "archivos_de_prueba/pruebas_catedra/" if modo_de_ejecucion == ARCHIVOS_CATEDRA else "archivos_de_prueba/pruebas_propias/"
    path_archivo = path_base + nombre_archivo

    soldados, ataques  = leer_batalla_txt(path_archivo)

    enemigos_liquidados, orden_de_ataques = planear_estrategia(soldados, ataques)

    imprimir_estrategia(enemigos_liquidados, orden_de_ataques, nombre_archivo)

def correr_pruebas(modo_de_ejecucion):
    if modo_de_ejecucion == PRUEBAS_ARCHIVOS_CATEDRA:
        correr_pruebas_sobre_estrategias(son_pruebas_propias=False)
    else:
        correr_pruebas_sobre_estrategias(son_pruebas_propias=True)


def main():
    modo_de_ejecucion = sys.argv[1]

    if (modo_de_ejecucion == ARCHIVOS_CATEDRA) or (modo_de_ejecucion == ARCHIVOS_PROPIOS):
        nombre_archivo = sys.argv[2]
        correr_algoritmo(modo_de_ejecucion, nombre_archivo)
    elif (modo_de_ejecucion == PRUEBAS_ARCHIVOS_CATEDRA) or (modo_de_ejecucion == PRUEBAS_ARCHIVOS_PROPIOS):
        correr_pruebas(modo_de_ejecucion)
    elif modo_de_ejecucion == GENERAR_GRAFICO:
        print("Generando grafico...")
        #generar_grafico()
    else:
        raise Exception("Modo de ejecución incorrecto")

if __name__ == '__main__':
    main()
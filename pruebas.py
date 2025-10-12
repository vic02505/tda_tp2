from ast import main
from algoritmo.estrategia import planear_estrategia
from lector_de_archivos.resultados_esperados import obtener_estrategias_esperadas, obtener_resultados_esperados
from lector_de_archivos.parser_de_batallas import leer_batalla_txt


def correr_pruebas_sobre_estrategias(son_pruebas_propias: bool):

    path_base_de_archivos = "archivos_de_prueba/"
    
    if not son_pruebas_propias:
        resultados_esperados = obtener_resultados_esperados(path_base_de_archivos + "pruebas_catedra/Resultados Esperados.txt")
        estrategias_esperadas = obtener_estrategias_esperadas(path_base_de_archivos + "pruebas_catedra/Resultados Esperados.txt")

        tests = [k for k in resultados_esperados.keys()]
        for test in tests:
            soldados, ataques = leer_batalla_txt("archivos_de_prueba/pruebas_catedra/" + test)
            cantidad, estrategia = planear_estrategia(soldados, ataques)
            esperado = resultados_esperados[test]
            estrategia_esp = estrategias_esperadas[test]
            ok_cantidad = cantidad == esperado
            ok_estrategia = estrategia == estrategia_esp
            print(f"{test}: calculado={cantidad} esperado={esperado} {'OK' if ok_cantidad else 'ERROR'}")
            print(f"  Estrategia: {'OK' if ok_estrategia else 'DIFERENTE'}")
        
        
    else:
        resultados_esperados = obtener_resultados_esperados(path_base_de_archivos + "pruebas_propias/Resultados Esperados.txt")
        estrategias_esperadas = obtener_estrategias_esperadas(path_base_de_archivos + "pruebas_propias/Resultados Esperados.txt")

        tests = [k for k in resultados_esperados.keys()]
        for test in tests:
            soldados, ataques = leer_batalla_txt("archivos_de_prueba/pruebas_propias/" + test)
            cantidad, estrategia = planear_estrategia(soldados, ataques)
            esperado = resultados_esperados[test]
            estrategia_esp = estrategias_esperadas[test]
            ok_cantidad = cantidad == esperado
            ok_estrategia = estrategia == estrategia_esp
            print(f"{test}: calculado={cantidad} esperado={esperado} {'OK' if ok_cantidad else 'ERROR'}")
            print(f"  Estrategia: {'OK' if ok_estrategia else 'DIFERENTE'}")
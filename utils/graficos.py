from algoritmo.estrategia import planear_estrategia
import random
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from .util import RUNS_PER_SIZE, time_algorithm
import time

# Seteamos la seed para reproducibilidad
random.seed(12345)
np.random.seed(12345)

# Genera listas de batallas
def generar_batallas(n):
    soldados = np.random.randint(1, 1000, n)
    ataques = np.random.randint(1, 5000, n)
    ataques.sort()
    return soldados.tolist(), ataques.tolist()

def generar_grafico():
    start = time.time()

    # Tamaños de entrada
    sizes = np.linspace(100, 5000, 20).astype(int)

    # Pregenerar todos los datos de entrada para cada tamaño y repetición (necesario para que cada vez que se generan batallas se use la misma seed)
    batallas_por_n = {
        n: [generar_batallas(n) for _ in range(RUNS_PER_SIZE)]
        for n in sizes
    }

    # Crear un get_args que devuelve los datos ya generados, en orden
    indices = {n: 0 for n in sizes}
    def get_args(n):
        idx = indices[n]
        indices[n] += 1
        return batallas_por_n[n][idx]

    # Medir tiempos usando util.py
    resultados = time_algorithm(planear_estrategia, sizes, get_args)

    end = time.time()
    print(f"Tiempo total para generar los resultados: {end - start:.4f} segundos")

    x = np.array(list(resultados.keys()))
    y = np.array(list(resultados.values()))

    # Ajuste por cuadrados mínimos: complejidad esperada O(n^2)
    def modelo_n2(n, c1, c2):
        return c1 * n**2 + c2
    
    #comentar el anterior y descomentar alguno de estos para ajustar por otro modelo
    # # O(nlogn)
    # def modelo_nlogn(n, c1, c2):
    #     return c1 * n * np.log(n) + c2
    
    # # O(n)
    # def modelo_n(n, c1, c2):
    #     return c1 * n + c2

    (c1, c2), _ = sp.optimize.curve_fit(modelo_n2, x, y)
    print(f"Ajuste encontrado: c1={c1}, c2={c2}")

    # c1 es la pendiente escalada del término n^2. Indica cuánto “crece” el tiempo de ejecución en función del tamaño n. Es la constante que acompaña a la complejidad teórica O(n^2).

    # c2 es un desfase o tiempo base. Representa un tiempo inicial “fijo” que el algoritmo tarda independientemente del tamaño (por ejemplo, overhead de iniciar la función).

    # Calcular errores
    y_pred = modelo_n2(x, c1, c2)

    # y_pred[i] es el tiempo que la curva ajustada dice que debería tomar el algoritmo para x[i].
    # y[i] es el tiempo que realmente tomó el algoritmo.

    # Error cuadrático total (||Ax - b||^2)
    r = np.sum((y_pred - y)**2)
    print(f"Error cuadrático total: {r}") # notacion cientifica
    print(f"Error cuadrático total con decimales: {r:.20f}") # con 20 decimales

    errores_abs = np.abs(y_pred - y)

    # Graficar tiempos vs curva ajustada
    plt.figure()
    plt.plot(x, y, "bo", label="Mediciones")
    plt.plot(x, y_pred, "r--", label="Ajuste $n^2$")
    plt.xlabel("Tamaño n")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de ejecución de planear_estrategia")
    plt.legend()
    plt.show()

    # Graficar error absoluto
    plt.figure()
    plt.plot(x, errores_abs, "g")
    plt.xlabel("Tamaño n")
    plt.ylabel("Error absoluto (s)")
    plt.title("Error del ajuste")
    plt.show()

# tda_tp2
Trabajo práctico #2 - TDA - Curso Buchwald-Genender
Repositorio del segundo trabajo práctico de la materia Teoría de Algoritmos. 

| Nombre           | Apellido      | Padrón   |
|------------------|---------------|----------|
| Víctor           | Zacarías      | 107080   |
| Carolina         | Aramayo       | 106260   |
| Francisco Nahuel | Tapia         | 107128   |

## Instrucciones de ejecución:

El programa consta de los siguientes modos de ejecución:

1. Archivos de la cátedra: Corre el algoritmo sobre alguno de los archivos de prueba provistos por la cátedra.
2. Pruebas sobre los archivos de la cátedra: Corre pruebas sobre los archivos provistos por la cátedra.
3. Archivos propios: Corre el algoritmo sobre archivos propios diseñados para estudiar algún caso particular.
4. Pruebas sobre archivos propios: Al igual que el modo #2 se usa para correr pruebas, pero sobre los archivos propios.
5. Generar gráficos: Se usa para generar gráficos de los tiempos de ejecución del algoritmo.

### Ejecución del algoritmo sobre algún archivo de datos:

1. Archivos de la cátedra:

    ```bash
    python3 main.py 1 <nombre_archivo>
    ```
    **NOTA:** nombre_archivo es el nombre de un archivo (e excepcion del archivo de salidas esperadas) del directorio
    archivos_de_prueba/pruebas_catedra. Por ejemplo una línea de ejecución válida es `python3 main.py 1 5.txt`.

2. Pruebas sobre archivos de la cátedra:

    ```bash
    python3 main.py 2
    ```

3. Archivos propios:

    ```bash
    python3 main.py 3 <nombre_archivo>
    ```
     **NOTA:** nombre_archivo es el nombre de un archivo (e excepcion del archivo de salidas esperadas) del directorio
    archivos_de_prueba/pruebas_propias. Por ejemplo una línea de ejecución válida es `python3 main.py 1 5.txt`.

4. Pruebas sobre archivos propios:
    
    ```bash
    python3 main.py 4
    ```

5. Generador de gráficos:

    ```bash
    python3 main.py 5
    ```
   **NOTA:**: Para generar los gráficos es necesario contar con las dependencias matplotlib, numpy y scipy. 
   Las versiones más avanzadas de ubuntu impiden descargar las dependencias de forma directa, por lo que es 
   necesario hacer uso de un venv en el que ejecutar el programa.

    No consideramos que fuese necesario agregar lógica para el manejo de dependencias a la entrega, ya que lo más 
    importante se encuentra en la ejecución del algoritmo y visualización de su salida. Por lo cual, el
    código que llama a la función generadora se encuentra comentado, al igual que el import de 
    la correspondiente función.
        
     En caso de querer generar gráficos, es necesario descomentar y bajarse las dependencias. Puede ser que una 
     dependencia adicional sea requerida (TkAgg).

# tda_tp2
Trabajo práctico #2 - TDA - Curso Buchwald-Genender
Repositorio del segundo trabajo práctico de la materia Teoría de Algoritmos. 

| Nombre           | Apellido      | Padrón   |
|------------------|---------------|----------|
| Víctor           | Zacarías      | 107080   |
| Carolina         | Aramayo       | 106260   |
| Francisco Nahuel | Tapia         | 107128   |

## Instrucciones de ejecución:

1. Para correr el algoritmo sobre un archivo con datos de BLABLA:

```bash
python3 main.py 1 <nombre_de_archivo>
```
**Nota:** Los nombres de archivos válidos son los que se encuentran en el directorio **archivos_de_prueba** del proyecto. Por ejemplo,
para correr el algoritmo sobre el archivo **10.txt** es necesario escribir desde la raíz del proyecto la línea 
de comandos `python3 main.py 1 10.txt`.

2. Para correr los tests sobre todos los archivos con BLABLA:

```bash
python3 main.py 2
```
# Análisis del problema
- Tenemos minutos de $1...n$. En el minuto $i$ llegan $x[i]$ soldados.
- Si ejecutamos un ataque en el minuto $k$, y el último ataque previo fue en el minuto $s$ (tomamos $s = 0$ si no hubo ataques antes), entonces pasó $j = k - s$ minutos de carga y el ataque elimina el $min( x[k], f(j) )$.
- Inicialmente no hay energía acumulada. Si ataco en el minuto 1 entonces $j = 1$ y la energía disponible es $f(1)$. Esto se puede modelar bien si consideramos que hubo un último ataque ficticio en $s = 0$.
- Queremos elegir un subconjunto de minutos en los que atacar para **maximizar la suma** de los soldados eliminados.

$f$ es monótona creciente.
## Recurrencia
Tenemos que:
- hallar la máxima cantidad de enemigos eliminados
- considerando sólo los minutos $1...k$.

Estoy en el problema *lo pongo, no lo pongo*. Es decir, tengo que atacar en $k$ o no atacar en $k$.

Entonces, definimos:
1. `M[K] = max cantidad de enemigos eliminados`

2. No atacar en $k$ = `M[K-1]` 
3. Atacar en $k$. Entonces tiene que existir un minuto $s$ (entre $0$ y $k-1$) que sea el último minuto donde se atacó antes de $k$ (si no hubo ninguno $s = 0$). Si el último ataque fue en $s$, el beneficio adicional por atacar en $k$ es $min(x[k],f(k-s))$ y el óptimo hasta $s$ es `M[s]`.

Entonces una opción es:
$$ M[s] + min(x[k],f(k-s)) $$


Planteo caso base:
$$M[0] = 0$$

Caso general:
$$M[k] = max(no\ atacar,atacar)$$
Donde no atacar es:
```math 
M[k-1]
```
Donde atacar es:
`agregar s pertenece [0,k-1]`
```math
max(M[s] + min(x[k],f(k-s)))
```

Entonces la ecuación de recurrencia es:
```math
M[0] = 0
\\
M[k] = max(M[k-1],max(M[s] + min(x[k],f(k-s)))) \ con \ k = 1...n
```
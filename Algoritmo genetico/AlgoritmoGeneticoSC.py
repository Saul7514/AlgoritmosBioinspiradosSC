import random

# Función de aptitud (fitness function)
def calcular_aptitud(individuo):
    # Esta función evalúa qué tan buena es una solución
    return sum(individuo)

# Función de selección de padres (tournament selection)
def seleccionar_padres(poblacion, aptitudes, tamano_torneo):
    torneo = random.sample(range(len(poblacion)), tamano_torneo)
    ganador_torneo = min(torneo, key=lambda i: aptitudes[i])
    return poblacion[ganador_torneo]

# Función de cruce (crossover)
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Función de mutación
def mutar(individuo, tasa_mutacion):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = 1 - individuo[i]
    return individuo

# Parámetros del algoritmo genético
tamano_poblacion = 10
tamano_genoma = 5
tamano_torneo = 3
tasa_cruce = 0.8
tasa_mutacion = 0.1
num_generaciones = 100

# Inicialización de la población
poblacion = [[random.randint(0, 1) for _ in range(tamano_genoma)] for _ in range(tamano_poblacion)]

# Ciclo principal del algoritmo genético
for generacion in range(num_generaciones):
    # Evaluación de la aptitud de cada individuo en la población
    aptitudes = [calcular_aptitud(individuo) for individuo in poblacion]

    # Selección de padres
    padres = [seleccionar_padres(poblacion, aptitudes, tamano_torneo) for _ in range(tamano_poblacion)]

    # Cruce
    descendencia = []
    for i in range(0, tamano_poblacion, 2):
        if random.random() < tasa_cruce:
            hijo1, hijo2 = cruzar(padres[i], padres[i + 1])
            descendencia.extend([hijo1, hijo2])
        else:
            descendencia.extend([padres[i], padres[i + 1]])

    # Mutación
    descendencia = [mutar(individuo, tasa_mutacion) for individuo in descendencia]

    # Reemplazo de la población antigua con la nueva descendencia
    poblacion = descendencia

# Obtener el mejor individuo después de todas las generaciones
mejor_individuo = max(poblacion, key=calcular_aptitud)

print("Mejor individuo:", mejor_individuo)
print("Aptitud:", calcular_aptitud(mejor_individuo))

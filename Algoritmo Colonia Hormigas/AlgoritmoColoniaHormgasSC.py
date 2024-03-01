import numpy as np
import random

class ColoniaHormigas:
    def __init__(self, distancias, num_hormigas, evaporacion, alfa=1, beta=2, feromona_inicial=1):
        self.distancias = distancias
        self.num_ciudades = len(distancias)
        self.num_hormigas = num_hormigas
        self.evaporacion = evaporacion
        self.alfa = alfa
        self.beta = beta
        self.feromona_inicial = feromona_inicial

        # Inicialización de feromonas
        self.feromonas = np.ones((self.num_ciudades, self.num_ciudades)) * feromona_inicial

    def ejecutar(self, iteraciones):
        mejor_camino = None
        mejor_distancia = np.inf

        for _ in range(iteraciones):
            caminos_hormigas = self._generar_caminos_hormigas()

            for camino in caminos_hormigas:
                distancia_camino = self._calcular_distancia(camino)
                if distancia_camino < mejor_distancia:
                    mejor_camino = camino
                    mejor_distancia = distancia_camino

                self._actualizar_feromonas(camino, distancia_camino)

            self._evaporar_feromonas()

        return mejor_camino, mejor_distancia

    def _generar_caminos_hormigas(self):
        caminos_hormigas = []
        for _ in range(self.num_hormigas):
            camino_hormiga = self._generar_camino_hormiga()
            caminos_hormigas.append(camino_hormiga)
        return caminos_hormigas

    def _generar_camino_hormiga(self):
        inicio = random.randint(0, self.num_ciudades - 1)
        camino = [inicio]
        ciudades_no_visitadas = set(range(self.num_ciudades))
        ciudades_no_visitadas.remove(inicio)

        while ciudades_no_visitadas:
            siguiente_ciudad = self._seleccionar_siguiente_ciudad(camino[-1], ciudades_no_visitadas)
            camino.append(siguiente_ciudad)
            ciudades_no_visitadas.remove(siguiente_ciudad)

        return camino

    def _seleccionar_siguiente_ciudad(self, ciudad_actual, ciudades_no_visitadas):
        probabilidades = self._calcular_probabilidades(ciudad_actual, ciudades_no_visitadas)
        return random.choices(list(ciudades_no_visitadas), weights=probabilidades)[0]

    def _calcular_probabilidades(self, ciudad_actual, ciudades_no_visitadas):
        feromonas_ciudades = self.feromonas[ciudad_actual, list(ciudades_no_visitadas)]
        visibilidad_ciudades = 1 / self.distancias[ciudad_actual, list(ciudades_no_visitadas)]
        probabilidades = (feromonas_ciudades ** self.alfa) * (visibilidad_ciudades ** self.beta)
        probabilidades /= np.sum(probabilidades)
        return probabilidades

    def _calcular_distancia(self, camino):
        distancia = 0
        for i in range(len(camino) - 1):
            distancia += self.distancias[camino[i], camino[i+1]]
        distancia += self.distancias[camino[-1], camino[0]]  # Añadir la distancia de regreso al inicio
        return distancia

    def _actualizar_feromonas(self, camino, distancia_camino):
        for i in range(len(camino) - 1):
            ciudad_actual, ciudad_siguiente = camino[i], camino[i+1]
            self.feromonas[ciudad_actual, ciudad_siguiente] += 1 / distancia_camino
            self.feromonas[ciudad_siguiente, ciudad_actual] += 1 / distancia_camino

    def _evaporar_feromonas(self):
        self.feromonas *= (1 - self.evaporacion)

# Ejemplo de uso
distancias = np.array([[0, 2, 9, 10],
                       [1, 0, 6, 4],
                       [15, 7, 0, 8],
                       [6, 3, 12, 0]])

num_hormigas = 10
evaporacion = 0.1
aco = ColoniaHormigas(distancias, num_hormigas, evaporacion)
mejor_camino, mejor_distancia = aco.ejecutar(iteraciones=100)

print("Mejor camino:", mejor_camino)
print("Mejor distancia:", mejor_distancia)

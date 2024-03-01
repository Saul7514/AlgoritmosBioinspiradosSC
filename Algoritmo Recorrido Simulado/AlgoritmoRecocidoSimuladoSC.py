import numpy as np

def simulated_annealing(cost_function, initial_solution, initial_temperature, cooling_rate, iterations):
    current_solution = initial_solution
    best_solution = current_solution
    current_cost = cost_function(current_solution)
    best_cost = current_cost
    temperature = initial_temperature

    for iteration in range(iterations):
        new_solution = generate_neighbor(current_solution)
        new_cost = cost_function(new_solution)

        if accept_solution(current_cost, new_cost, temperature):
            current_solution = new_solution
            current_cost = new_cost

        if new_cost < best_cost:
            best_solution = new_solution
            best_cost = new_cost

        temperature = cool_temperature(temperature, cooling_rate)

    return best_solution, best_cost

def generate_neighbor(solution):
    # Genera un vecino aleatorio. Esta función debería ajustarse según el problema.
    # Por ejemplo, podrías cambiar aleatoriamente un elemento en una lista.
    return np.random.permutation(solution)

def accept_solution(current_cost, new_cost, temperature):
    if new_cost < current_cost:
        return True
    probability = np.exp((current_cost - new_cost) / temperature)
    return np.random.rand() < probability

def cool_temperature(temperature, cooling_rate):
    return temperature * cooling_rate

# Ejemplo de uso
def cost_function(solution):
    # Función de costo de ejemplo. Puedes cambiar esto según tu problema.
    return np.sum(np.square(solution))

# Parámetros iniciales
initial_solution = np.array([2.0, 3.0, -1.0, 4.0])
initial_temperature = 1000.0
cooling_rate = 0.95
iterations = 1000

# Aplicar el algoritmo de Recocido Simulado
best_solution, best_cost = simulated_annealing(cost_function, initial_solution, initial_temperature, cooling_rate, iterations)

print("Mejor solución encontrada:", best_solution)
print("Costo de la mejor solución:", best_cost)

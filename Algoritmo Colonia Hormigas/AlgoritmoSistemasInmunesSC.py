import random

class Linfocito:
    def __init__(self, tamaño):
        self.receptor = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(tamaño))

    def reconocer(self, antígeno):
        return sum(1 for a, b in zip(self.receptor, antígeno) if a == b)

class SistemaInmune:
    def __init__(self, tamaño_población, tamaño_receptor):
        self.población = [Linfocito(tamaño_receptor) for _ in range(tamaño_población)]

    def atacar(self, antígeno):
        reconocimientos = [linfocito.reconocer(antígeno) for linfocito in self.población]
        mejor_linfocito = self.población[reconocimientos.index(max(reconocimientos))]
        if max(reconocimientos) > 0:  # Si al menos un linfocito reconoció el antígeno
            print(f"El antígeno {antígeno} fue reconocido y eliminado por el linfocito con receptor {mejor_linfocito.receptor}")
        else:
            print(f"El antígeno {antígeno} no fue reconocido por ningún linfocito")

# Ejemplo de uso
sistema = SistemaInmune(tamaño_población=10, tamaño_receptor=5)
antígenos = ["ABCD", "WXYZ", "MNOP"]

for antígeno in antígenos:
    sistema.atacar(antígeno)

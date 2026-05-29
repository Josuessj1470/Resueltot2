class Caja:
    def __init__(self, nombre, peso, soles):
        self.nombre = nombre
        self.peso = peso
        self.soles = soles

    def relacion(self):
        return self.soles / self.peso


def mochila_voraz(cajas, capacidad):

    cajas.sort(key=lambda x: x.relacion(), reverse=True)

    peso_total = 0
    soles_totales = 0

    print("\nCajas seleccionadas:")

    for caja in cajas:

        if peso_total + caja.peso <= capacidad:

            peso_total += caja.peso
            soles_totales += caja.soles

            print(f"- {caja.nombre} COMPLETA")
            print(f"  Peso: {caja.peso}")
            print(f"  Soles: {caja.soles}")

        else:

            espacio_restante = capacidad - peso_total

            if espacio_restante > 0:

                fraccion = espacio_restante / caja.peso

                peso_fraccion = caja.peso * fraccion
                soles_fraccion = caja.soles * fraccion

                peso_total += peso_fraccion
                soles_totales += soles_fraccion

                print(f"- {caja.nombre} FRACCIÓN ({fraccion:.2f})")
                print(f"  Peso tomado: {peso_fraccion:.2f}")
                print(f"  Soles obtenidos: {soles_fraccion:.2f}")

            break


    print("\nRESULTADOS FINALES")
    print(f"Peso total: {peso_total:.2f}")
    print(f"Soles totales: {soles_totales:.2f}")


m = float(input("Ingrese el peso máximo de la mochila: "))

cajas = [
    Caja("Caja A", 10, 60),
    Caja("Caja B", 20, 100),
    Caja("Caja C", 30, 120)
]

mochila_voraz(cajas, m)
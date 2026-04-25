import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0   


equipo1 = Equipo("Equipo 1")
equipo2 = Equipo("Equipo 2")


def Puntos():
    return random.randint(10, 28)


def PuntosExtras():
    return random.randint(0, 6)


def RegistrarSet(ganador):
    global equipo1, equipo2

    if ganador == 1:
        equipo1.setGanados += 1
        print(f" {equipo1.nombre} gana el set (Sets: {equipo1.setGanados})")
    else:
        equipo2.setGanados += 1
        print(f" {equipo2.nombre} gana el set (Sets: {equipo2.setGanados})")

    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        return True

    if equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        return True

    return False


def JugarPartido():
    global equipo1, equipo2

    print(f"\n Partido: {equipo1.nombre} vs {equipo2.nombre}")

    sets1 = 0
    sets2 = 0

    while sets1 < 3 and sets2 < 3:

        p1 = Puntos()
        p2 = Puntos()

        print(f"Puntos iniciales → {p1} - {p2}")

        
        while p1 < 25 and p2 < 25:
            extra1 = PuntosExtras()
            extra2 = PuntosExtras()

            p1 += extra1
            p2 += extra2

            print(f"Extras aplicados → {equipo1.nombre}: +{extra1}, {equipo2.nombre}: +{extra2}")
            print(f"Puntaje actual → {p1} - {p2}")

        while p1 == p2:
            extra1 = PuntosExtras()
            extra2 = PuntosExtras()

            p1 += extra1
            p2 += extra2

            print(f"Empate → extras → {equipo1.nombre}: +{extra1}, {equipo2.nombre}: +{extra2}")
            print(f"Nuevo puntaje → {p1} - {p2}")

        if p1 >= 25 and p1 > p2:
            sets1 += 1
            RegistrarSet(1)
        elif p2 >= 25 and p2 > p1:
            sets2 += 1
            RegistrarSet(2)

    print(f"Resultado final: {sets1} - {sets2}")

    if sets1 > sets2:
        print(f" {equipo1.nombre} ganó el partido")
    else:
        print(f" {equipo2.nombre} ganó el partido")


def ResultadoTorneo():
    print("\n RESULTADOS FINALES:")
    print(f"{equipo1.nombre} - Ganados: {equipo1.partidosGanados} | Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre} - Ganados: {equipo2.partidosGanados} | Perdidos: {equipo2.partidosPerdidos}")


n = int(input("¿Cuántos partidos jugarán?: "))

for i in range(n):
    JugarPartido()

ResultadoTorneo()
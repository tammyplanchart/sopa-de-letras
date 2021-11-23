class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
    
    def sumar_punto(self):
        self.puntos = self.puntos + 1
    
    def mostrar_puntaje(self):
        print("Jugador: " + self.nombre)
        print("Puntaje: " + str(self.puntos))
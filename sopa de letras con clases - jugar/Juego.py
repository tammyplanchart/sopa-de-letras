from Jugador import Jugador
from Tablero import Tablero
class Juego:
    def __init__(self, usuario, archivo):
        self.jugador = Jugador(usuario)
        self.tablero = Tablero(archivo)
        self.palabras_encontradas = []

    def jugar(self):
        palabra_candidata = ""
        while len(self.palabras_encontradas) < self.tablero.obtener_cantidad_de_palabras(): #verifico si la cantidad de palabras encontradas esmenor a la cantidad de palabras dentro del diccionario
            self.tablero.imprimir()
            palabra_candidata = input("Ingresa la palabra que encontraste: ")
            if palabra_candidata == "fin": #si la palabra que ingresa el usuario (palabra_candidata) es igual a fin entonces corta el bucle con el break.
                break
            encontro_la_palabra = self.tablero.buscar_palabra(palabra_candidata)
            if(encontro_la_palabra):
                print("Felicidades! Encontraste una palabra")
                self.palabras_encontradas.append(palabra_candidata)
                self.jugador.sumar_punto()
                self.tablero.marcar_palabra(palabra_candidata)
            else:
                print("Palabra incorrecta")

    def terminar_juego(self):
        print("-----FIN DEL JUEGO-----")

        self.jugador.mostrar_puntaje()

        print("Palabras encontradas: ")
        for palabra_encontrada in self.palabras_encontradas:
            print("* " + palabra_encontrada)
        
        print("Palabras no encontradas: ")
        for palabra_no_encontrada in self.tablero.palabras_no_encontradas(self.palabras_encontradas):
            print("* " + palabra_no_encontrada)
import csv

class Tablero:
    def __init__(self, nombre_del_archivo):
        self.matriz = []
        self.diccionario = {}

        with open(nombre_del_archivo + ".csv", "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.matriz.append(row)
                # cuando instancio el array le coloco una matriz vacia y a medida voy leyendo el archivo le voy agregando cosas 
                # a la matriz
                # uso el array que cree en un inicio

        with open(nombre_del_archivo + "_solucion.csv", "r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.diccionario[row.get("palabra")] = {
                    "x_inicial": int(row.get("x_inicial")),
                    "y_inicial": int(row.get("y_inicial")),
                    "x_final": int(row.get("x_final")),
                    "y_final": int(row.get("y_final"))
                }
                # instancio el diccionario vacio y lo lleno con las palabras de la solucion
    def imprimir(self):
        for fila in self.matriz:
            for letra in fila:
                print (letra, end=" | ")
            print("\n")

    def buscar_palabra(self, palabra_candidata):
        palabra_encontrada = self.diccionario.get(palabra_candidata)
        return (palabra_encontrada != None)

    def palabras_no_encontradas(self, palabras_encontradas):
        return sorted(set(self.diccionario.keys()) - set(palabras_encontradas))

    def marcar_palabra(self, palabra):
        posicion = self.diccionario.get(palabra)# conel get accedo a la palabra en el diccionario
        if posicion.get("y_inicial") == posicion.get("y_final"):
            for i in range(posicion.get("x_inicial"), posicion.get("x_final") + 1):
                self.matriz[posicion.get("y_inicial")][i] = self.matriz[posicion.get("y_inicial")][i].upper()
# fila 43 son las palabras encontradas en ubicación vertical
        else:
            for i in range(posicion.get("y_inicial"), posicion.get("y_final") + 1):
                self.matriz[i][posicion.get("x_inicial")] = self.matriz[i][posicion.get("x_inicial")].upper()

    def obtener_cantidad_de_palabras(self):
        return len(self.diccionario) #puedo acceder al diccionario y ver la cantidad de palabras que hay dentro.
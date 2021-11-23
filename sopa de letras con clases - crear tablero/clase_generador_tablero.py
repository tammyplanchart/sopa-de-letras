import random
from copy import deepcopy
import string

class Generador_tableros:
    def completar_tablero(self, tablero): 
        for index_fila, fila in enumerate(tablero):
            for index_columna, letra in enumerate(fila):
                if letra == ".":
                    tablero[index_fila][index_columna] = random.choice(string.ascii_letters).lower()

    def insertar_al_diccionario(self, diccionario, palabra, posicion):
        diccionario[palabra] = posicion
        return diccionario

    def generar_lugar_aleatorio(self, N, palabra):
        # horizontal = True
        # vertical = False
        es_horizontal = bool(random.getrandbits(1))

        # al derecho = True
        # al reves = False
        al_derecho = bool(random.getrandbits(1))

        if (es_horizontal):
            columna_inicial = random.randint(0, N - len(palabra))
            fila_inicial = random.randint(0, N - 1)
        else:
            columna_inicial = random.randint(0, N - 1)
            fila_inicial = random.randint(0, N - len(palabra))

        return (es_horizontal, al_derecho, fila_inicial, columna_inicial)

    def insertar_palabra(self, palabra, tablero, lugar):
        (es_horizontal, al_derecho, fila_inicial, columna_inicial) = lugar

        # creo un tablero temporal que puedo modificar sin que se modifique el tablero real
        # voy a ir modificando el tablero temporal letra por letra y si falla, hago un return False
        tablero_temporal = deepcopy(tablero)

        # si la palabra esta al reves, la doy vuelta. casa -> asac
        if not al_derecho:
            palabra = palabra[::-1]

        for (index, letra) in enumerate(palabra):
            # calculo la fila y columna donde insertar la letra
            fila_actual = fila_inicial
            columna_actual = columna_inicial
            if es_horizontal:
                columna_actual = columna_inicial + index
            else:
                fila_actual = fila_inicial + index

            # chequeo si justo en ese lugar ya habia otra letra
            letra_previa = tablero_temporal[fila_actual][columna_actual]
            if (letra_previa != "." and letra_previa != letra):
                return (tablero_temporal, False, None)

            # agrego la letra en la fila y columnas que calcule
            tablero_temporal[fila_actual][columna_actual] = letra

        # se termino el for, por lo que ya se inserto la palabra entera en el tablero
        posicion = {"x_inicial": columna_inicial, "y_inicial": fila_inicial, "x_final": columna_actual, "y_final": fila_actual}
        return (tablero_temporal, True, posicion)

    def generar(self, N, palabras):
        # tablero es un array de filas
        tablero = []
        for index in range(N):
            tablero.append(["."] * N)

        diccionario = {}

        # 1. generar lugar aleatorio para insertar la palabra la tablero. horizontal/vertical, arriba hacia abajo o al reves, x inicial, y inicial
        # 2. intentar insertar la palabra en el lugar aleatorio
        # 3. si se pudo insertar, volver al punto 1 y repetir hasta insertar todas las palabras
        # 4. si no se pudo insertar, volver al punto 1 y repetir hasta poder insertarla
        # 5. una vez que se hayan insertado todas las palabras, llenar los espacios vacios del tablero con letras al azar
        palabras_insertadas = 0
        while palabras_insertadas < len(palabras):
            palabra_actual = palabras[palabras_insertadas]
            lugar = self.generar_lugar_aleatorio(N, palabra_actual)
            print("LUGAR GENERADO", lugar)
            (nuevo_tablero, inserto_la_palabra_correctamente, posicion) = self.insertar_palabra(palabra_actual, tablero, lugar)
            if inserto_la_palabra_correctamente:
                print("INSERTO", palabras[palabras_insertadas], inserto_la_palabra_correctamente)
                diccionario = self.insertar_al_diccionario(diccionario, palabra_actual, posicion)
                tablero = nuevo_tablero
                palabras_insertadas = palabras_insertadas + 1

        self.completar_tablero(tablero)
        return (tablero, diccionario)

    
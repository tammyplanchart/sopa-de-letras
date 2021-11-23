from typing import TextIO, final


class Obtener_datos:
    def nombre_archivo(self, texto):
        return len(texto) <= 30

    def validacion_de_datos(self, numero):
        return int (numero) >= 15

    def pedir_dato(self, texto, funcion_de_validacion):
        while True:
            texto_ingresado = input(texto)
            if funcion_de_validacion(texto_ingresado):
                return texto_ingresado
            print("ERROR")

    def obtener_datos_tablero(self):
        n = int(self.pedir_dato(
            "Ingrese la cantidad de filas y columnas de la sopa de letras (debe ser mayor o igual a 15): ",
            self.validacion_de_datos
        ))

        n_sobre_3 = n // 3

        def validar_palabra(palabra):
            return len(palabra) <= n_sobre_3 and len(palabra) > 0

        lista_de_palabras = []

        while len(lista_de_palabras) < n_sobre_3:
            palabra = self.pedir_dato("Ingrese una palabra (hasta " + str(n_sobre_3) + " caracteres): ", validar_palabra)
            if palabra == "fin":
                break
            else: 
                lista_de_palabras.append(palabra)
        
        nombre_del_archivo = self.pedir_dato("Ingrese el nombre del archivo: ", self.nombre_archivo)

        return (n, lista_de_palabras, nombre_del_archivo)
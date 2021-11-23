import os.path

class Obtener_datos:
    def nombre_archivo(self, archivo):
        return os.path.isfile(archivo+".csv")

    def validacion_de_nombre(self, nombre):
        return len(nombre) < 40

    def pedir_dato(self, texto, funcion_de_validacion):
        while True:
            texto_ingresado = input(texto)
            if funcion_de_validacion(texto_ingresado):
                return texto_ingresado
            print("ERROR")

    def obtener_datos_del_usuario(self):
        nombre = self.pedir_dato(
            "Ingrese un nombre menor o igual a 40 caracteres: ",
            self.validacion_de_nombre
        )

        archivo = self.pedir_dato(
            "Ingrese el nombre del archivo: ",
            self.nombre_archivo
        )

        return (nombre, archivo)
from clase_generador_tablero import Generador_tableros
from Clase_obtener_datos import Obtener_datos
from clase_Escritor import Escritor
def main():
    obtener_datos = Obtener_datos()
    (n, lista_de_palabras, nombre_del_archivo) = obtener_datos.obtener_datos_tablero()

    generador_tableros = Generador_tableros()
    (tablero, diccionario) = generador_tableros.generar(n, lista_de_palabras)
     
    escritor = Escritor()
    escritor.escribir_tablero(tablero, nombre_del_archivo) 
    escritor.escribir_solucion(diccionario, nombre_del_archivo) 

main()
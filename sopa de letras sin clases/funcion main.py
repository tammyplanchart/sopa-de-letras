from pedir_datos_tablero import pedir_datos_tablero
from generar_tablero import generar_tablero, mostrar_tablero
from escribir_tablero import escribir_juego

def main ():
    (n, lista_de_palabras, nombre_del_archivo) = pedir_datos_tablero()
    (tablero, diccionario) = generar_tablero(n, lista_de_palabras)
    mostrar_tablero(tablero)
    escribir_juego(tablero, diccionario, nombre_del_archivo)

main()
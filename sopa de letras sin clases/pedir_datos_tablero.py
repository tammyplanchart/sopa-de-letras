from pedir_dato import pedir_dato

def nombre_archivo(texto):
    return len(texto) <= 30

def validacion_de_datos(numero):
    return int (numero) >= 15

def pedir_datos_tablero():
    n = int(pedir_dato(
        "Ingrese la cantidad de filas y columnas de la sopa de letras (debe ser mayor o igual a 15): ",
        validacion_de_datos
    ))

    n_sobre_3 = n // 3

    def validar_palabra(palabra):
        return len(palabra) <= n_sobre_3 and len(palabra) > 0

    lista_de_palabras = []

    while len(lista_de_palabras) < n_sobre_3:
        palabra = pedir_dato("Ingrese una palabra (hasta " + str(n_sobre_3) + " caracteres): ", validar_palabra)
        if palabra == "fin":
            break
        else: 
            lista_de_palabras.append(palabra)
    
    nombre_del_archivo = pedir_dato("Ingrese el nombre del archivo: ", nombre_archivo)

    return (n, lista_de_palabras, nombre_del_archivo)
def pedir_dato(texto, funcion_de_validacion):
    while True:
        texto_ingresado = input(texto)
        if funcion_de_validacion(texto_ingresado):
            return texto_ingresado
        print("ERROR")

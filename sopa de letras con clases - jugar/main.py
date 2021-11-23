from Obtener_datos import Obtener_datos 
from Juego import Juego 
def main():
    obtener_datos = Obtener_datos()
    (usuario, archivo) = obtener_datos.obtener_datos_del_usuario()

    juego = Juego(usuario, archivo)
    juego.jugar()
    juego.terminar_juego()

main()
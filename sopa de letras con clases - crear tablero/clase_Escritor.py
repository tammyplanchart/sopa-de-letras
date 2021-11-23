import csv
 
class Escritor:

  def escribir_tablero (self, matriz, nombre_del_archivo):
    with open(nombre_del_archivo + ".csv", "w", newline='') as file:
      writer = csv.writer(file)
      writer.writerows(matriz)

  def escribir_solucion(self, diccionario, nombre_del_archivo):
    with open(nombre_del_archivo + "_solucion.csv", "w", newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['palabra', 'x_inicial', 'y_inicial', 'y_final', 'x_final'])
    
      array_nuevo = list(diccionario.keys())
      for key in array_nuevo:

        # palabra, x_inicial, y_inicial, y_final, x_final
        array_palabra = [key, diccionario.get(key).get("x_inicial"), diccionario.get(key).get("y_inicial"), diccionario.get(key).get("y_final"), diccionario.get(key).get("x_final") ] #la palabra de la sopa de letras es la clave del diccionario y key es la clave del diccionario q estoy usando en este caso
        writer.writerow(array_palabra)

"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Luis", "apellidos": "Alvarez"}
print("Imprimir diccionario")

lista = [diccionario,diccionario2]


for l in lista:
    midiccionario = l
    print("Mi nombre es: %s y mi apellido es %s" %
          (midiccionario["nombre"], midiccionario["apellidos"]))


#print("Mi nombre es: %s y mi apellido es %s" % (diccionario[l], diccionario[l]))
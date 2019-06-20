"""
    @reroes
    Ejemplo de manejo  de Excepciones
    http://docs.python.org.ar/tutorial/3/errors.html

"""

from librerias.misexcepciones import NumeroNegativosError, \
        TamanioDatosPersonalesError

numero = input("Ingrese el número de empleados: \n")
numero = int(numero)
contador = 0

print("Ingreso de datos de empleado\n")
while(contador < numero):

    try:
        nombre = input("Ingreso su nombre :\n")
        nota1 = input("Ingreso de nota 1 :\n")
        nota2 = input("Ingreso de nota 2 :\n")
        nota1 = int(nota1)
        nota2 = int(nota2)
        if (nota1 < 0) or (nota2 < 0):
            raise NumeroNegativosError("No se puede ingresar valor menore a cero")
        if len(nombre)==1:
            raise TamanioDatosPersonalesError("El tamaño de la cadena %s, debe" \
                    "ser mayor a 1 caracter " % nombre)
        promedio = int(nota1) / int(nota2)
        print("Los datos ingresados son: \nNombre: %s\nNota1: %d \nNota2: %d"\
                "\nPromedio: %f" % (nombre, int(nota1), int(nota2), promedio))
        contador = contador + 1
    except TypeError as ex:
        print("Algo paso en el programa (TypeError)\n")
        print(ex)
        print(type(ex))
    except NumeroNegativosError as ex:
        print("Algo paso en el programa (NumeroNegativosError)\n")
        print(ex)
        print(type(ex))
    except TamanioDatosPersonalesError as ex:
        print("Algo paso en el programa (TamanioDatosPersonalesError)\n")
        print(ex)
        print(type(ex))
    except Exception as ex:
        print("Algo paso en el programa (Exeption)\n")
        print(ex)
        print(type(ex))
    
print("Gracias por su información")


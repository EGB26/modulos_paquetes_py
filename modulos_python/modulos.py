"""
import modulos1

print(modulos1.multiplicar(7, 8))
print(modulos1.dividIr(7, 8))
print(modulos1.restar(7, 8))
print(modulos1.sumar(7, 8))
"""
#from modulos1 import * /todos los modulos

from modulos1 import sumar, restar, saludo
#importación desde paquete
import mi_paquete.funciones_matematicas #forma larga
import mi_paquete.funciones_matematicas as func_mat #forma larga con alias
#from mi_paquete.funciones_matematicas import calcular_factorial, frase
#importación de un sub-paquete
from mi_paquete.sub_paquete.funciones_avanzadas import contar_letras
print(restar(7, 8))
print(sumar(7, 8))

print(saludo)
#print(calcular_factorial(5))
#print(mi_paquete.funciones_matematicas.calcular_factorial(5)) #forma larga
print(func_mat.calcular_factorial(5)) #forma larga con alias
#print(frase)
print(mi_paquete.funciones_matematicas.frase) #forma larga
print(func_mat.frase) #forma larga con alias

texto = 'gracias totales'
print(contar_letras(texto))

#vamos a agregar varias cosas

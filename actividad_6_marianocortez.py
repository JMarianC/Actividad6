# -*- coding: utf-8 -*-
"""Actividad 6_MarianoCortez.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fc1NBY9jwlA5wax_AyNHUNpmlCSzgwjm

Actividad N°6 Cuenta

Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase: 

-> Un constructor.

-> mostrar(): Muestra los datos de la cuenta.

-> ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

-> retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos
"""

#Definimos la Clase:

class Cuenta:

  titular = "Titular" #Atributo de Clase

  #EL Cosnstructor

  def __init__(self, cuenta, nombre, cantidad=0):

#Atributos de instancia

    self.nombre=nombre
    self.cantidad=cantidad
    self.cuenta=cuenta

#Metodos sin argumentos:

  def mostrar(self):                        #Info de la Cuenta
    print(f"Cuenta Nº: {self.cuenta}")
    print(f"Nombre y Apellido: {self.nombre}")
    
    
#Metodo con argumento:

  def ingresar(self, ingreso): #Lo que se ingresa
    self.ingreso=ingreso
    if ingreso >0:
      print(f"Cantidad Ingresada: {self.ingreso}")

#--------------------
      
  def retirar(self, retiro): #Lo que se retira
    self.retiro=retiro
    print(f"Cantidad Retirada: {self.retiro}")

#------------------

    if (self.cantidad + self.ingreso - self.retiro) < 0:
      print("Usted debe:", (self.retiro - (self.cantidad + self.ingreso)))
    
    else:
      print("En su cuenta hay:", (self.cantidad + self.ingreso- self.retiro))

cuenta1= Cuenta(12589, "Juan Cuchuflito", 200.80)

cuenta1.mostrar()
print(f"Es {cuenta1.titular}")

cuenta1.ingresar(300)
cuenta1.retirar(700)

cuenta2 = Cuenta(132697, "Lorena Chula", 1500)
cuenta2.mostrar()
print(f"Es {cuenta2.titular}")

cuenta2.ingresar(450)
cuenta2.retirar(600)
#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


class Tienda
tipo = electrodomesticos


def __init__(self, nombre_tienda, direccion_tienda, num_empleados, venta_ultimos_3_meses):
    self_nombre = nombre_tienda
    self_direccion = direccion_tienda
    self_num_empl = num_empleados
    self_venta_3_meses = venta_ultimos_3_meses
 ##met para calcular tlv
def calcular_ventas_totales(self):
    return self.sum.self_ventas_3_meses


#metodo para ver nombre y direccion
def nombre_direccion(self):
    return "nombre" + self_nombre + ",direccion" + self_direccion



# Método para obtener las ventas del último mes
def ventas_ultimo_mes(self):
    return self_ventas_3_meses[-1] if self_ventas_3_meses else 0


 # Reescribe el atributo de ventas con el aumento proyectado
def proyectar_ventas(self, inversion_marketing):
    if inversion_marketing < 1000:
    return factor = 1.2
else:
return factor =1.6
    

##reescribe el atributo
self.ventas_ultimos_3_meses = [venta * factor for venta in self.ventas_ultimos_3_meses]
return self.ventas_ultimos_3_meses                             

# Crear tres tiendas con datos inventados
tienda1 = Tienda("Tienda A", "Avenida Siempre Viva 742", 10, [20000, 22000, 25000])
tienda2 = Tienda("Tienda B", "Calle Falsa 123", 8, [18000, 19000, 20000])
tienda3 = Tienda("Tienda C", "Avenida del Sol 456", 12, [30000, 31000, 32000])

# Comprobar la funcionalidad de la clase en una tienda
print(tienda1.obtener_nombre_y_direccion())
print(f"Ventas Totales: {tienda1.calcular_ventas_totales()}")
print(f"Media Ventas/Empleado: {tienda1.media_ventas_por_empleado()}")
print(f"Ventas Último Mes: {tienda1.ventas_ultimo_mes()}")
print(f"Proyección de Ventas con Inversión de 1500: {tienda1.proyectar_ventas(1500)}")

# Calcular las ventas del último mes de todas las tiendas
for tienda in [tienda1, tienda2, tienda3]:
    print(f"Ventas del último mes en {tienda.nombre_tienda}: {tienda.ventas_ultimo_mes()}")

# Imprimir los nombres de las tiendas cuya dirección contiene "Avenida"
for tienda in [tienda1, tienda2, tienda3]:
    if "Avenida" in tienda.direccion:
        print(f"Tienda en Avenida: {tienda.nombre}")


# In[ ]:


class Perro 
def __init__(self, raza_perro, color = marron, velocidad = 0, dueno = none):
    self.raza = raza_perro
    self.color = color
    self.velocidad = 0
    self.dueno = dueno
    self.orejas = 2
    self.patas = 4
    sel.ojos = 2
##metodo para que el perro ladre
def ladrar(self, sonido_perro = ""):
    return (f"guau: {sonido_perro}")


##metodo para que pare

def parar(self):
    self.velocidad == 0
    print(f"el perro se ha parado")


#metodo para qeu el perro camine
def andar(self, aumento_de_velocidad):
    self.velocidad +=aumento_de_velocidad


## metodo parar que el perro ladre
def ladrar(self, sonido_perro =""):
    return (f"guau {sonido_perro}")


# Método para verificar el estado actual del perro (opcional para facilitar pruebas)

def __str__(self):
    return(f"raza perro: {self.raza}", f"color perro: {self.color}", f"velocidad es: {self.velocidad}", "el dueno es: 
           {self.dueno if self.dueno else "sin dueno"}

def __self__(self):
    return(f"raza perro: {self.raza}", f"color perro: {self.color}", f"velocidad es: {self.velocidad}", F"el dueno es: 
    {self.dueno if self.dueno else "no dueno"}")


#crea un perro raza labrador
mi_perro = perro(raza"labrador")
print(mi_perro) #muestra todos los atributos de mi_perro

#para al perro
mi_perro.velocidad()
self.velocidad == 0


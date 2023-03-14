
#Trabajo de Arturo
#Entrada

n1 = int(input('Ingrese un primero número: '))
n2 = int(input('Ingrese un segundo número: '))

#Proceso

if n1 > n2:
    n3 = n1
    print('El número mayor es: ', n3)
else:
    n3 = n2
    print('El número mayor es: ', n3)
    
    
# Parte dos por Arthur Yoshioka

b = n3 % 2

if b == 0:
    print("Es un numero par porque tiene residuo 0")
else:
    print("Es un numero impar porque no tiene residuo 0")

#Trabajo 3 por Javier Mayorga
#Proceso

i = 1

while i <= n3:
    print(i)
    i += 1
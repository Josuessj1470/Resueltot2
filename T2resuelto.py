import random

n = int(input("¿De qué tamaño quieres la matriz? (ejemplo: 11): "))

matriz = []                     

for i in range(n):                 
    fila = []                     
    for j in range(n):             
        numero = random.randint(99, 999)
        fila.append(numero)      
    matriz.append(fila)          

print("\nMatriz generada:")

for i in range(n):              
    for j in range(n):             
        print(str(matriz[i][j]).rjust(4), end="") 
    print()                      

lista_plana = []

for i in range(n):             
    for j in range(n):           
        lista_plana.append(matriz[i][j])  
def contar_multiples(lista):
    if len(lista) == 1:
        if lista[0] % 5 == 0 or lista[0] % 7 == 0:
            return 1
        else:
            return 0
    mitad = len(lista) // 2
    parte_izquierda = lista[0:mitad]    
    parte_derecha   = lista[mitad:]      

    resultado_izq = contar_multiples(parte_izquierda)
    resultado_der = contar_multiples(parte_derecha)

    return resultado_izq + resultado_der

total = contar_multiples(lista_plana)

print("\nCantidad de números múltiplos de 5 o 7:", total)
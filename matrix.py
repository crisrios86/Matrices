# print("::::::::::matrix como lista anidada con enteros::::::::")

# consumo = [[3,6,9,8], 
#           [5,8,6,5],
#           [8,6,2,4]]

# for lista in consumo:
#     print("[", end = " ")
#     for elemento in lista:
#         print( elemento, end=" ")
#     print("]")

# print("::::::::::matrix como lista anidada con decimales::::::::")

# consumo_1 = [[3,6,9,8], 
#           [5,8,6,5],
#           [8,6,2,4]]

# for lista in consumo_1:
#     print("[", end = " ")
#     for elemento in lista:
#         print("{:8.2f}".format(elemento), end=" ")
#     print("]")

# print("::::::::::::::::creacion matriz nula:::::::::::::::::::::")

# # def matrix_nula(filas,columnas):
# #     mx_0=[[0]*filas]*columnas
# #     for fila in mx_0:
# #         print(fila)

# # matrix_nula(10,15)

# print(":::::::::::::::::::::::otra forma::::::::::::::::")

# def matrix_nula(filas,columnas):
#     mx_0 = []
#     for i in range(filas):
#         mx_0.append([0]*columnas)
#     for fila in mx_0:
#         print(fila)  

# #matrix_nula(10,15)

# a = matrix_nula(10,15)

# print(":::::::::::::::::::cambio de algun elemto de la matrix:::::::::::::::")


# mx_0 = []
# for i in range(10):
#     mx_0.append([0]*15)

# mx_0[2][3]=2

# for fila in mx_0:
#      print(fila)  


#print(":::::::::::::::::::programa que cree una matrix con los datos introducidos uno a uno:::::::::::::::")

# filas = int(input("introduce el numero de filas: "))
# columnas = int(input("introduce el numero de columnas: "))

# matrix =[]

# for i in range(filas):
#     matrix.append([])
#     for j in range(columnas):
#         valor = float(input("Fila {} , Columna {} : ".format(i+1 ,j+1)))
#         matrix[i].append(valor)

# print()
# for fila in matrix:
#     print("[", end = " ")
#     for elemento in fila:
#         print("{:8.2f}".format(elemento), end=" ")
#     print("]")

# print()


# print(":::::::::::::::::::suma de matrices:::::::::::::::")

# def suma_matrices(m1,m2):
#     #  numero de filas y columnas sea iguales en las dos matrices a sumar
#     if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        
#         m3=[]
#         for i in range(len(m1)):
#             m3.append([])
#             for j in range(len(m1[0])):#columnas
#                  m3[i].append(m1[i][j] + m2[i][j]) 
               
#         return m3
#     else:
#         return None

# a = [[1,1,1,1,2], 
#      [1,1,1,1,2],
#      [1,1,1,1,2]]

# b = [[1,1,1,1], 
#      [1,1,1,1],
#      [1,1,1,1]]

# c = suma_matrices(a,b)

# if c == None:
#     print("no se pueden sumar")

# else:
#     for fila in c:
#         print("[" , end= " ")
#         for elemento in fila:
#             print(elemento, end = " ")
#         print("]")


# print(":::::::::::::::::::multiplicar  matrices:::::::::::::::")

# a = [[2,2,2,8],
#      [2,2,1,9],]

# b = [[2,1],
#      [1,2],
#      [2,3],
#      [2,5]]

# def multiplicar_matrices(m1,m2):

#     if len(m1[0])==len((m2)):
#         m3=[]
#         for i in range(len(m1)):
#             m3.append([])
#             for j in range(len(m2[0])):
#                 m3[i].append(0)



#         for i in range(len(m1)):  
#             for j in range(len(m2[0])):
#                 for k in range(len(m1[0])):
#                      m3[i][j] += m1[i][k] * m2[k][j]
#         return m3
#     else:
#         return None

# c = multiplicar_matrices(b,a)   

# if c==None:
#     print("no se puede multiplicar")
# else:
#     for fila in c:
#         print("[", end = " ")
#         for elemento in fila:
#             print(elemento, end = " ")
#         print("]")
    

print(":::::::::::::::::::matrix transpuesta:::::::::::::::")       

m1 = [[2,2,2,8],
      [2,2,1,9]]

m2= [[2,2],
     [2,2],
     [2,1],
     [8,9]]

def transponer(m):
   
    t =[]
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t

transpuesta = transponer(m2)

print("::::::::::::::::MATRIZ ORIGINAL ::::::::::::::::")

for fila in m2:
    for elemento in fila:
        print(elemento, end =" ")
    print()

print("::::::::::::::::TRANSPUESTA ::::::::::::::::")


for fila in transpuesta:
    for elemento in fila:
        print(elemento, end =" ")
    print()

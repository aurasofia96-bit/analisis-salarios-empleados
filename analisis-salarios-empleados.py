#Constantes
numero_trabajadores=10
#Variables
datos = []
contador=[['A',0,0,0,0,0,0],['B',0,0,0,0,0,0],['C',0,0,0,0,0,0]]
# [grupo, suma_salarios, cantidad, suma_edades, prom_salario, prom_edad, incremento]
#Pedido de datos
for i in range(numero_trabajadores):
    print()
    trabajador = []
    print(f'Datos para el trabajador {i+1}')
    salario=float(input('Salario:')) #/////////SALARIO/////////////
    while salario <= 0:
        print('Error:dato no valido')
        salario=float(input('Salario:'))
    trabajador.append(salario)
    antiguedad=int(input('Años de antigüedad:')) # //////////ANTIGUEDAD/////
    while antiguedad < 0:
        print('Error:dato no valido')
        antiguedad=int(input('Años de antigüedad:'))
    trabajador.append(antiguedad)
    edad=int(input('Edad:')) #//////// EDAD/////
    while edad <= 0:
        print('Error:dato no valido')
        edad=int(input('Edad:'))
    trabajador.append(edad)
    #Clasificar por grupos /////////////////////////
    if trabajador[1] <= 2: 
        trabajador.append('A')
        contador[0][1] += trabajador[0]
        contador[0][2] += 1
        contador[0][3] += trabajador[2]
    elif trabajador[1] > 8:
        trabajador.append('C')
        contador[2][1] += trabajador[0]
        contador[2][2] += 1
        contador[2][3] += trabajador[2]
    else:
        trabajador.append('B')
        contador[1][1] += trabajador[0]
        contador[1][2] += 1
        contador[1][3] += trabajador[2]
    datos.append(trabajador)
# Calcular promedios
for i in range(3):
    if contador[i][2] > 0:
        contador[i][4] += (contador[i][1]/contador[i][2])
        contador[i][5] += (contador[i][3]/contador[i][2])
# Incremento por grupo
if contador[0][2] > 0:
    if contador[0][4] > 2000000:
        contador[0][6] += 0.04
    else:
        contador[0][6] += 0.07
if contador[1][2] > 0:
    if contador[1][4] > 2400000:
        contador[1][6] += 0.05
    else:
        contador[1][6] += 0.08
if contador[2][2] > 0:
    if contador[2][4] > 3000000:
        contador[2][6] += 0.06
    else:
        contador[2][6] += 0.1
#Mostrar resultados
for i in range(3):
    print(f'''Grupo {contador[i][0]}:
      • Promedio de salarios: {round(contador[i][4])}
      • Suma total de salarios: {contador[i][1]}
      • Porcentaje de incremento: {int(contador[i][6]*100)}%
      • Promedio de edades: {round(contador[i][5])}''')
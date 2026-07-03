#Constantes
numero_trabajadores=10
#Variables
datos = []
salario_A=salario_B=salario_C=contador_A=contador_B=contador_C=edad_A=edad_B=edad_C=0
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
        salario_A+=trabajador[0]
        contador_A+= 1
        edad_A+=trabajador[2]
    elif trabajador[1] > 8:
        trabajador.append('C')
        salario_C+=trabajador[0]
        contador_C+= 1
        edad_C+=trabajador[2]
    else:
        trabajador.append('B')
        salario_B+=trabajador[0]
        contador_B+= 1
        edad_B+=trabajador[2]
    datos.append(trabajador)
print(datos)
# Calcular promedios
if contador_A == 0:
    salario_promedio_A = 0
    edad_promedio_A = 0
else:
    salario_promedio_A=salario_A/contador_A
    edad_promedio_A=edad_A/contador_A
if contador_B == 0:
    salario_promedio_B = 0
    edad_promedio_B = 0
else:
    salario_promedio_B=salario_B/contador_B
    edad_promedio_B=edad_B/contador_B
if contador_C == 0:
    salario_promedio_C = 0
    edad_promedio_C = 0
else:
    salario_promedio_C=salario_C/contador_C
    edad_promedio_C=edad_C/contador_C
# Incremento por grupo
if salario_promedio_A > 2000000:
    incremento_A=0.04
else:
    incremento_A=0.07
if salario_promedio_B > 2400000:
    incremento_B=0.05
else:
    incremento_B=0.08
if salario_promedio_C > 3000000:
    incremento_C=0.06
else:
    incremento_C=0.10
#Mostrar resultados
print(f'''Grupo A:
      • Promedio de salarios: {salario_promedio_A}
      • Suma total de salarios: {salario_A}
      • Porcentaje de incremento: {int(incremento_A*100)}%
      • Promedio de edades: {edad_promedio_A}''')
print(f'''Grupo B:
      • Promedio de salarios: {salario_promedio_B}
      • Suma total de salarios: {salario_B}
      • Porcentaje de incremento: {int(incremento_B*100)}%
      • Promedio de edades: {edad_promedio_B}''')
print(f'''Grupo C:
      • Promedio de salarios: {salario_promedio_C}
      • Suma total de salarios: {salario_C}
      • Porcentaje de incremento: {int(incremento_C*100)}%
      • Promedio de edades: {edad_promedio_C}''')

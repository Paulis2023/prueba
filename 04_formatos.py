# formatos de impresion
edad = 60
estatura = 1.8
print('la edad es:', edad)
print('la estatura es:', estatura)
# primer manera de usar texto concatenado con variables
print('la edad es:', edad, 'y la estatura es:', estatura)
# 2da manera de formato (mas usada)
print(f'la edad es:{edad} y la estatura es: {estatura}')
# 3ra manera de uso de formato
print('la edad es:{} y la estatura es: {}'.format(edad, estatura))
print('la edad mas la estatura es:', edad + estatura)
print(f'la edad mas la estatura es: {edad + estatura}')
print('la edad mas la estatura es:{}'.format(edad + estatura))
suma = edad + estatura
print(f'la edad mas la estatura es:{suma}')

# CONDICIONAL if
adivinar = 42
number = int(input('Sr usuario digite un número:'))
if (number > adivinar):
  print('VERDADERO')
else:
  print('FALSO')

number = int(input('Sr usuario digite un número:'))
if (number > adivinar):
  print('Bajele el volumen')
elif (number < adivinar):
  print('Subale el volumen')
else:
  print("VERDADERO")
# IF ANIDADO 2
if (number >= adivinar):
  if (number > adivinar):
    print('Coloque un número menor')
  else:
    print('Acertado!!!')
else:
  print('Coloque un número mayor')
# FIN DEL IF

print('La instrucción "IF" termino.')

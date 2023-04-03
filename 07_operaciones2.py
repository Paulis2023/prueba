# OPERACIONES RELACIONALES O DE COMPARACIÓN
number = int(input('Digite un número: '))
number > 3
print(number > 3)
number >= 3
print(number >= 3)
print(number < 3)
print(number <= 3)
print(number == 3)
print(number != 3)

# OPERACIONES LOGICAS
print("operaciones logicas")
# TRUE(1) / FALSE (0)
# CONJUNCIÓN(and &)
print("conjunción(and):")
# valor1 and valor 2
print(True & True)
print((number >= 3) and True)
print((number >= 3) and False)
print((number >= 3) and False and False)
print(number >= 3 & False & False)
print(True and True and True)

# disyuncion (or , |)
print("disyunción (or):")
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print(number > 3 or number < 10)

# negación (not, ~)
print('negación :')
print(~ True)
# or exclusiva (^)
print('Or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)
# OPERACIONES DE PERTENENCIA
# in
print('operador in:')
nombre = 'Cesar Quintero'
print('Q' in nombre)
print('z' in nombre)

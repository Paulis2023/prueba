num = [99, 34, 25, 56, 72]
print(num)
num[1] = 88
print(num)
# num = [99, 88, 25, 56, 72]
#función insert
print('uso de la función insert:')
num.insert(1, 77)
print(num)
#num = [99, 77, 88, 25, 56, 72]
# función append
print('uso de la función append:')
num.append(100)
print(num)
#num = [99, 77, 88, 25, 56, 72, 100]
num2 = [9, 8, 7]
# funcion extend
print('uso de la funcion extend:')
num.extend(num2)
print(num)
# num = [99, 77, 88, 25, 56, 72, 100,9,8,7]
# función remove
print('uso de la función remove:')
num.remove(100)
print(num)
# num = [99, 77, 88, 25, 56, 72, 9,8,7]
# función pop
print('uso de la función pop:')
num.pop(2)
print(num)
# num = [99, 77, 25, 56, 72, 9,8,7]
# función del:
print('uso de la funcion del:')
del num[0]
print(num)
# num = [77, 25, 56, 72, 9,8,7]
#función clear
print('uso de la función clear:')
num2.clear()
print(num2)

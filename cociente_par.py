# crear una funcion para aplicar un ciclo repetitivo y funcion recursiva
d = int(input('ingrese divisor:'))
d2 = int(input('ingrese dividendo:'))

if d % 2 == 0 and d2 % 2 == 0:
    c = d / d2
    print ('el cociente es:', int(c))

if d % 2 != 0 and d2 % 2 != 0 :
    print('dividendo y divisor impar')

elif d % 2 != 0 or d2 % 2 != 0:
    print ('divisor', d)
    print ('dividendo', d2)
    print ('solo numeros pares')






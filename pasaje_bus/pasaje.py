p = float(input('ingrese valor del pasaje:'))
e = int(input('ingrese su edad:'))

if e> 7 and e <65:
    print ('pagar pasaje completo')
    if p == 0.30:
        print ('pasaje completo')
    elif p < 0.30:
        print('pasaje incompleto')
        f = 0.30 - p
        print('faltan:', f)
    elif p > 0.30:
        print('dar vuelto')
        v = p - 0.30
        print('su vuelto es de:', v)


if e < 7 or e > 65:
    print ('pagar medio pasaje')
    if p == 0.15:
        print ('pasaje completo')
    elif p < 0.15:
        print ('pasaje incompleto')
        f2 = 0.15 - p
        print ('faltan:', f2)
    elif p > 0.15:
        print ('dar vuelto')
        v2 = p - 0.15
        print('su vuelto es:', v2)



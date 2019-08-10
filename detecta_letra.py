a = 3
z = input()
l = len(z)
y, i = 'e', l
print('')

while i > 0:
    if z[l - i] == y:
            print('existe e en la posicion:', l - i)
    else:
        print('no existe e en la posicion:', l - i)

    i -= 1
   
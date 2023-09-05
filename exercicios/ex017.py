print('\033[34mCALCULO DE HIPOTENUSA\033[m')

c1 = float(input('Cateto oposto(cm): '))
c2 = float(input('Cateto adjescente(cm): '))
hi = (((c1 * c1) + (c2 * c2)) ** (1/2))

print(f'\033[32mHIPOTENUSA:\033[m \033[35m{hi}\033[m')

from math import hypot

print('\033[34mCALCULO DE HIPOTENUSA\033[m')
co = float(input('Cateto oposto(cm): '))
ca = float(input('Cateto adjescente(cm): '))
hi = hypot(co, ca)
print(f'\033[32mHIPOTENUSA:\033[m \033[35m{hi:.2f}\033[m')

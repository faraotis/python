num = int(input('Digite um numero inteiro para ver sua TABUADA: '))
cont = 0
print(('=' * len(str(num * 10))) + ('=' * len(str(num))) + '=========')
for c in range(10):
    cont += 1
    print(f'{num} x {cont:2} = {num * cont}')
print(('=' * len(str(num * 10))) + ('=' * len(str(num))) + '=========')

from time import sleep

num = int(input('Digite um numero inteiro: '))
print(f'Analizando o numero {num}.')
print('Calculando')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.', end='')
sleep(0.3)
print('.')
sleep(0.3)
print(f'''ANTECESSOR: {num-1}
SUCESSOR: {num+1}''')


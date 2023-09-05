from random import shuffle

print('\033[33mSORTEAR ORDEM\033[m')
nomes = []
for c in range(4):
    nomes.append(str(input(f'{c + 1}st NOME: ')))
shuffle(nomes)
print('ORDEM SORTEADA: ', end='')
for d in range(4):
    print(f'{nomes[d]} ', end='')

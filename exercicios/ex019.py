from random import choice

alunos = []
print('Sorteio de alunos')
for c in range(4):
    alunos.append(str(input(f'Nome do {c + 1}st aluno: ')))
sorteio = choice(alunos)
print(f'O aluno sorteado foi: \033[31m{sorteio}\033[m')

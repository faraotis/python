salario = float(input('Salario do funcionario: R$'))
desconto = (salario * 15) / 100
print(f'Remuneracao do funcionario:\n'
      f'ANTES: {salario:.2f} R$\n'
      f'DEPOIS: {salario + desconto:.2f} R$')

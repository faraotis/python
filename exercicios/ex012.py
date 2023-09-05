preco = float(input('Valor do produto(R$): '))
desconto = (preco * 5) / 100
print(f'Preco original: {preco} R$\n'
      f'Preco com desconto: {preco - desconto:.2f} R$')

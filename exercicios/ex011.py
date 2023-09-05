altura = float(input('Altura da Parede(m): '))
largura = float(input('Largura da Parede(m): '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensao de {altura}x{largura}m e sua area e de {area:.1f}m²\n'
      f'Para pintar essa parede, sera necessario {tinta:.1f}L de tinta.')

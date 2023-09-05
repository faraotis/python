celsius = float(input('Informe uma Temperatura em Celsius: '))
escolha = vars()
while escolha != 0 or escolha != 1:
    escolha = int(input('Escolha uma conversao:\n'
                        '0 - KELVIN\n'
                        '1 - FARENHEIT\n'))
    if escolha == 0:
        print(f'{celsius}ºC = {celsius + 273.15}K')
        break
    if escolha == 1:
        print(f'{celsius}ºC = {(celsius * 1.8) + 32:.1f}ºF')
        break
    if escolha != 0 or escolha != 1:
        print('\033[31mOpcao invalida, tente novamente...\033[m')
        escolha = vars()

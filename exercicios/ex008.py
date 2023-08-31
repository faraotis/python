m = float(input('Uma distancia em metros: '))

print(f'''
{m / 1000}km
{m / 100}hm
{m / 10}dam
{round(m / 0.1)}dm
{m * 100:.0f}cm
{m * 1000:.0f}mm
''')

from math import sin, cos, tan, radians

print('\033[34mDados de um ANGULO\033[m')
angulo = float(input('ANGULO: '))
print(f'''\033[32mSENO:\033[m \033[35m{sin(radians(angulo)):.2f}\033[m
\033[32mCOSSENO:\033[m \033[35m{cos(radians(angulo)):.2f}\033[m
\033[32mTANGENTE:\033[m \033[35m{tan(radians(angulo)):.2f}\033[m''')

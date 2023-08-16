from random import randint
from time import sleep

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'x', 'w', 'y', 'z']

num = randint(0, 25)
letra = alfabeto[num]


print('\033[34mgerando sua letra...\033[m')
sleep(0.5)
print(f"\033[32m{letra}\033[m")

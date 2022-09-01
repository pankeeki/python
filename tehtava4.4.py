from random import randint
from random import seed
seed()
luku = randint(1,10)
while (True):
    arvaus = float(input('Arvaa numero: '))
    if arvaus < luku:
        print('Liian pieni.')
    elif arvaus > luku:
        print('Liian suuri.')
    elif arvaus == luku:
        break

print('Oikein arvattu!')

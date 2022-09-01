import math
import random
from random import seed
seed()

N = int(input('Montako pistettä laitetaan?')) ## arvottujen pisteiden kokonaismäärä
n = 0 ## ympyrän sisään jäävien pisteiden kokonaismäärä
kierrokset = 0
while kierrokset <= N:
    x = float(random.random())
    y = float(random.random())
    if x ** 2 + y ** 2 < 1:
        n = n + 1
    kierrokset = kierrokset + 1
likiarvo = 4*n/N
print(f'Likiarvo on {likiarvo}')
import math
le = float(input('Montako leiviskää? '))
n = float(input('Montako naulaa? '))
lu = float(input('Montako luotia? '))

n = n + le*20
lu = lu + n*32
massa = lu*13.3
kg = math.floor(massa/1000)
g = massa - kg*1000

print(f'Massa nykymittojen mukaan: {kg} kg ja {g} g.')
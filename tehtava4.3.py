min = None
max = None
while (True):
    syote = input('Anna numero: ')
    if syote == '':
        print(f'Antamistasi numeroista pienin oli {min} ja suurin oli {max}')
        break
    else:
        syote = float(syote)
    if min == None:
        min = syote
        max = syote
    if syote < min:
        min = syote
    if syote > max:
        max = syote
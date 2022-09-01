while (True):
    tuumat = float(input('Anna tuumamäärä: '))
    sentit = tuumat / 2.54
    if sentit < 0:
        break
    print(f'antamasi mitta on senttimetreinä {sentit}.')
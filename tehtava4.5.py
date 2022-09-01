otunnus = 'python'
osalasana = 'rules'
yritykset = int(1)
while yritykset < 5:
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    if tunnus == otunnus and salasana == osalasana:
        print('Tervetuloa')
        break
    elif yritykset == 5:
        print('Pääsy evätty.')
        break
    else:
        print('Virheelliset tunnukset, yritä uudestaan')
        yritykset = yritykset + 1

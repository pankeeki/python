otunnus = 'python'
osalasana = 'rules'
yritykset = int(0)
while yritykset < 6:
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    if tunnus == otunnus and salasana == osalasana:
        print('Tervetuloa')
        break
    else:
        print('Virheelliset tunnukset, yritä uudestaan')
        yritykset = yritykset + 1
if yritykset > 5:
    print('Pääsy evätty.')
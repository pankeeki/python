s = input('Mikä on biologinen sukupuolesi? (M/N) ')
h = int(input('Mikä on hemoglobiiniarvosi (g/l)? '))

if s == 'N':
    if h < 117:
        print('Hemoglobiiniarvosi on alhainen.')
    elif 117 <= h < 175:
        print('Hemoglobiiniarvosi on normaali.')
    else:
        print('Hemoglobiiniarvosi on korkea.')
elif s == 'M':
    if h < 134:
        print('Hemoglobiiniarvosi on alhainen.')
    elif 134 <= h < 195:
        print('Hemoglobiiniarvosi on normaali.')
    else:
        print('Hemoglobiiniarvosi on korkea.')
else:
    print('Virheellinen syöte. Käytäthän suuria kirjaimia vastauksessasi.')
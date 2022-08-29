kuhacm = float(input('Mikä on kuhasi pituus senttimetreinä? '))
puuttuva = float(37 - kuhacm)
if kuhacm >= 37:
    print('Hyvä homma!')
else:
    print(f'Kuhasi on {puuttuva} cm liian pieni, palautahan se järveen kasvamaan.')
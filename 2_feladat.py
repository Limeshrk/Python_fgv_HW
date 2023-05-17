names = ['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']

def name_counter(name_list, name):
    count = 0
    for i in range(0,len(name_list)):
        if name_list[i] == name:
            count += 1
    print(f'{name} ennyiszer fordul elő: {count}')
    return count

name_counter(names, 'Pista')

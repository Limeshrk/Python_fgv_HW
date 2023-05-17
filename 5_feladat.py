import math

def grouping(list):
    sorted_names = sorted(list)
    group_count = math.floor(len(sorted_names)/2) #Ha páratlan számú, akkor egész értéket néz, és a második csoport lesz eggyel nagyobb
    group1 = []
    group2 = []
    for i in range(0,group_count):
        group1.append(sorted_names[i])
    for i in range(group_count,len(sorted_names)):
        group2.append(sorted_names[i])
    print('1. csoport:')
    print(*group1, sep="\n")
    print('2. csoport:')
    print(*group2, sep="\n")
    

names = ['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda',
         'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']    

grouping(names)
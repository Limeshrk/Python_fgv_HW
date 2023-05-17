def number_div_find(start,finish,oszthato,nem_oszthato):
    numbers = []
    for n in range(start,finish+1):
        if n % oszthato == 0 and n % nem_oszthato != 0:
            numbers.append(n)
    print(numbers) #kiírja a számokat
    return numbers #vissza adja a számokat visszatérési értékként

number_div_find(100, 1000, 5, 8)
print('Kérek egy számot:')
text = input()
print(f'A megadott érték: {text}')

def convert_to_number(text):
    converted_text = int(text)
    return converted_text

num = convert_to_number(text)

def print_hello(num):
    counter = 0
    for i in range(0,num):
        counter = i+1
        print(f"{counter}. Helló!")

print_hello(num)

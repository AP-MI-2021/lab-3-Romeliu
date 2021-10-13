def is_perfect_square(numar: int) -> bool:
    #verifica daca variabila numar este patrat perfect; returneaza true daca este, false in caz contrar
    perfect_square = False
    if(numar == 1):
        return True
    else:
        i = 2
        while i * i < numar:
            i += 1
        if i * i == numar:
            perfect_square = True
    return perfect_square

def test_is_perfect_square():
    assert is_perfect_square(49) == True
    assert is_perfect_square(23) == False
    assert is_perfect_square(121) == True
    assert is_perfect_square(341) == False
    assert is_perfect_square(289) == True 

def all_perfect_squares(lista):
    #verifica daca toate numerele din lista sunt patrate perfecte
    for numar in lista:
        if not is_perfect_square(numar):
            return False
    return True

def get_longest_all_perfect_squares(lst : list[int]) -> list[int]:
    #genreaza toate secventele posibile, retine toate secventele care sunt formate doar din patrate perfecte, iar apoi o returneaza pe cea mai lunga
    lista_secvente = []

    for start in range(0, len(lst)):
        for end in range(start + 1, len(lst)):
            if all_perfect_squares(lst[start:end]):
                lista_secvente.append(lst[start:end])

    secventa_maxima = []

    for secventa in lista_secvente:
        if len(secventa) >= len(secventa_maxima):
            secventa_maxima = secventa
    return secventa_maxima

def number_of_1_bits(numar: int) -> int:
    #returneaza numarul de biti de 1 din reprezentarea binara a numarului primit
    numar_de_1_biti = 0
    while numar:
        if numar % 2 == 1:
            numar_de_1_biti += 1
        numar = numar // 2
    return numar_de_1_biti

def all_same_number_of_1_bits(lista):
    #returneaza True daca toate numerele din lista primita au acelasi numar de biti de 1 in reprezentarea binara
    element = 0
    for numar in lista:
        if element == 0:
            number_of_1_bits_var = number_of_1_bits(numar)
        if not number_of_1_bits(numar) == number_of_1_bits_var:
            return False
        element += 1
    return True

def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    #returneaza cea mai lunga secventa cu proprietatea ca toate numerele au acelasi numar de biti de 1 in reprezentarea lor binara
    lista_secvente = []

    for start in range(0, len(lst)):
        for end in range(start + 1, len(lst)):
            if all_same_number_of_1_bits(lst[start:end]):
                lista_secvente.append(lst[start:end])
    
    secventa_maxima = []

    for secventa in lista_secvente:
        if len(secventa) >= len(secventa_maxima):
            secventa_maxima = secventa
    return secventa_maxima

def show_ps(lista):
    secventa_pp = get_longest_all_perfect_squares(lista)
    if len(secventa_pp) != 0:
        secventa_pp_str = ''
        for pp in secventa_pp:
            secventa_pp_str += str(pp) + ' '
        print(f'Cea mai lunga secventa cu proprietatea ca toate numerle au acelasi numar de biti de 1 in reprezentarea lor binara este: {secventa_pp_str}')
    else:
        print('Nu exista nicio secventa formata doar din patrate perfecte')

def show_bit(lista):
    secventa_bit = get_longest_same_bit_counts(lista)
    if len(secventa_bit) != 0:
        secventa_bit_str = ''
        for bit in secventa_bit:
            secventa_bit_str += str(bit) + ' '
        print(f'Cea mai lunga secventa cu proprietatea ca toate numerle sunt patrate perfecte este: {secventa_bit_str}')
    else:
        print('Nu exista nicio secventa formata doar din numere care au acelasi numar de biti de 1 in reprezentarea lor binara')

def read_list():
    lista = input("introduceti numerele din lista separate printr-un spatiu: ")
    lista_str = lista.split(' ')
    lista_int = []
    for element in lista_str:
        lista_int.append(int(element))
    print('Lista inregistrata cu succes')
    return lista_int

def number_of_divs(numar: int) -> int:
    #returneaza numarul de divizori proprii ai unui numar
    divizori = 0
    for div in range(2, numar // 2 + 1):
        if numar % div == 0:
            divizori += 1
    return divizori

def test_number_of_divs():
    assert number_of_divs(2) == 0
    assert number_of_divs(4) == 1
    assert number_of_divs(15) == 2
    assert number_of_divs(72) == 10

def same_number_of_divs(lista) -> bool:
    #returneaza true daca toate numerele din lista au acelasi numar de divizori, fals in caz contrar
    numar_de_divizori = number_of_divs(lista[0])
    index = 0
    for element in lista:
        if index != 0:
            if number_of_divs(element) != numar_de_divizori:
                return False
        index += 1
    return True

def get_longest_same_div_count(lst: list[int]) -> list[int]:
    #returneaza o lista care contine cea mai lunga secventa de numere care au acelasi numar de divizori
    lista_secvente = []

    for start in range(0 ,len(lst)):
        for end in range(start + 1, len(lst)):
            if same_number_of_divs(lst[start:end]):
                lista_secvente.append(lst[start:end])

    secventa_maxima = []

    for secventa in lista_secvente:
        if len(secventa) >= len(secventa_maxima):
            secventa_maxima = secventa   
    return secventa_maxima

def show_div(lista):
    secventa_div = get_longest_same_div_count(lista)
    if len(secventa_div) != 0:
        secventa_div_str = ''
        for div in secventa_div:
            secventa_div_str += str(div) + ' '
        print(f'Cea mai lunga secventa cu proprietatea ca toate numerle au acelasi numar divizori este: {secventa_div_str}')
    else:
        print('Nu exista nicio secventa formata din numere care au acelasi numar')

def menu():
    #printeaza meniul
    print('''Optiuni:
    1. Citire lista
    2. Determinarea celei mai lungi secvente cu proprietatea ca toate numerle sunt patrate perfecte
    3. Determinarea celei mai lungi secvente cu proprietatea ca toate numerle au acelasi numar de biti de 1 in reprezentarea lor binara
    4. Determinarea celei mai lungi secvente cu proprietatea ca toate numerle au acelasi numar de divizori
    x. Inchide aplicatia
    ''')
    lista_numere = []
    optiune = input('Alegeti optiunea: ')
    while optiune != 'x':
        if optiune == '1':
            lista_numere = read_list()
        elif optiune == '2':
            show_ps(lista_numere)
        elif optiune == '3':
            show_bit(lista_numere)
        elif optiune == '4':
            show_div(lista_numere)
        else:
            print("Introduceti o optiune valida")
        optiune = input('Alegeti optiunea: ')

def main():
    test_is_perfect_square()
    test_number_of_divs()
    menu()

main()
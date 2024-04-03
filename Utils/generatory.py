import random

def generate_nip():
    weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)

    while True:
        numbers = [
            random.randint(1, 9),
            random.randint(0, 9),
            random.randint(1, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9)
        ]
        control_number = sum([i * j for i, j in zip(numbers, weights)]) % 11
        if control_number < 10:
            break

    numbers.append(control_number)

    return "".join(map(str, numbers))

def generate_regon():
    weights = (8, 9, 2, 3, 4, 5, 6, 7)

    while True:
        numbers = [
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
        ]
        control_number = sum([i * j for i, j in zip(numbers, weights)]) % 11
        if control_number < 10:
            break
        elif control_number == 10:
            control_number = 0
            break

    numbers.append(control_number)

    return "".join(map(str, numbers))

def generate_do():
    weights = (7, 3, 1, 7, 3, 1, 7, 3)

    letters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
    letters_weights = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
                       "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
                       "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    let4do = [random.choice(letters_list), random.choice(letters_list), random.choice(letters_list)]
    lw = []
    for l in let4do:
        lw.append(letters_weights[l])

    numbers = [
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9),
    ]
    do_weight = lw + numbers
    control_number = sum([i * j for i, j in zip(do_weight, weights)]) % 10
    do = let4do + numbers
    do.insert(3, control_number)
    nr_dowodu = ''.join(str(x) for x in do)
    return nr_dowodu


def generate_ppe(osd):
    maski = {
        'PGE Dystrybucja S.A. Oddział Białystok': 'PL_ZEBB_xxxxxxxxxx_xx',
        'PGE Dystrybucja S.A. Oddział Lublin': 'PL_LUBD_xxxxxxxxxx_xx',
        'PGE Dystrybucja S.A. Oddział Łódź - Miasto': 'PLLZEDxxxxxxxxxxxx',
        'PGE Dystrybucja S.A. Oddział Łódź - Teren': 'PLZELDxxxxxxxxxxxx',
        'PGE Dystrybucja S.A. Oddział Rzeszów': '480548xxxxxxxxxxxx',
        'PGE Dystrybucja S.A. Oddział Skarżysko-Kamienna': 'PL_ZEOD_xxxxxxxxxx_xx',
        'PGE Dystrybucja S.A. Oddział Warszawa': 'PL_ZEWD_xxxxxxxxxx_xx',
        'PGE Dystrybucja S.A. Oddział Zamość': 'PLZKEDxxxxxxxxxxxx',
        'TAURON Dystrybucja S.A. (Kraków)': '59032242xxxxxxxxxx',
        'TAURON Dystrybucja S.A. (Wrocław)': '59032241xxxxxxxxxx',
        'TAURON Dystrybucja S.A. (Gliwice)': '59032240xxxxxxxxxx',
        'Enea Operator Sp. z o.o.': '5903106xxxxxxxxxxx',
        'Energa Operator S.A.': '5902438xxxxxxxxxxx',
        'Innogy Stoen Operator Sp. z o.o.': 'PL000001xxxxxxxxxxxxxxxxxxxxxxxxx',
        'PKP Energetyka S.A.': 'PL_PKPE_xxxxxxxxxx_xx',
        'POLENERGIA Dystrybucja Sp. z o.o.': 'PLPOLDxxxxxxxxxxxxxx',
        'Elco Energy Sp. z o.o.': 'PLELCOSCCxxxx',
        'ELSEN S.A.': 'ELSN_xxxxxxx',
        'Energia Euro Park Sp. z o.o.': 'EPP_xxxxx',
        'Energomedia Sp. z o.o.': 'EMID_xxxxxxxxxx',
        'Energoserwis Kleszczów Sp. z o.o.': 'PL_KLEO_xxxxxxxxxx_xx',
        'ESV Wisłosan Sp. z o.o.': 'WISL_xxxxxxxxxx_xx',
        'Przedsiębiorstwo Energetyczne ESV S.A.': 'ESVD_xxxxxxxxxx_xx',
        'Green Lights Dystrybucja Sp. z o.o.': 'GLDxxxxxxx',
        'Green Lights Sp. z o.o.': 'GLIxxxxxxx',
        'Green Lights Holding Sp. z o.o.': 'GLHxxxxxxx',
        'Grupa Energia Obrót GE Spółka z o.o. Spółka komandytowa': '2_xxxx_xxxxx',
        'Grupa Energia GE Spółka z o.o. Spółka komandytowa': '1_xxxx_xxxxx',
        'Miejska Energetyka Cieplna Sp. z o.o.': 'PExxx',
        'Plus Energia Sp. z o.o.': 'PExxxxxxxxxx',
        'Power 21 Sp. z o.o.': 'PLPOWER21xxxxxxxxxxxxxxxxx',
        'Terawat Dystrybucja Sp. z o.o.': 'PLTEDYxxxxxxxxxxxxxxxxxxxxxxxxxx'
    }

    maska_osd = maski.get(osd, "Nieznany OSD")
    kod_ppe = ""
    for l in maska_osd:
        if l != "x":
            kod_ppe += l
        else:
            l = str(random.randint(0, 9))
            kod_ppe += l

    return kod_ppe

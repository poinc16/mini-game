import main_extra
import random
import os


def create_character():
    your_name = name()
    your_element = choose_element()
    your_power = choose_power(your_element[0])
    your_max_dmg = max_dmg()

    your_hero = main_extra.Hero(
        your_name, your_element[1], your_power, your_max_dmg)
    return your_hero


def name():
    while True:
        print()
        my_name = input('Por favor, digite o seu nome: ')
        v = verification(my_name)
        if v == 'yes':
            os.system('cls')
            return my_name


def choose_element():
    while True:
        print()
        print(f'Escolha um elemento dentre os listados abaixo (digite o número referente ao elemento): ')
        for n, el in main_extra.element.items():
            print(f'[{n}] : {el}')
        choice_element = input('Faça sua escolha: ')

        try:
            choice_element = int(choice_element)
        except ValueError:
            print('Por favor, digite um valor válido!')
            print()
        else:
            if choice_element > 0 and choice_element < 5:
                element_name = de_encryption_element(choice_element)
                v = verification(element_name)
                if v == 'yes':
                    os.system('cls')
                    return choice_element, element_name
            else:
                print('Por favor, digite um valor válido!')
                print()


def de_encryption_element(x):
    if x == 1:
        element_name = list(main_extra.element.values())
        return element_name[0]
    elif x == 2:
        element_name = list(main_extra.element.values())
        return element_name[1]
    elif x == 3:
        element_name = list(main_extra.element.values())
        return element_name[2]
    else:
        element_name = list(main_extra.element.values())
        return element_name[3]


def choose_power(n):
    print()
    print('Agora escolha o poder referente ao seu elemento: ')
    if n == 1:
        while True:
            for x, sp in main_extra.super_power1.items():
                print(f'[{x}] : {sp}')
            choice_power = input('Faça sua escolha: ')
            try:
                choice_power = int(choice_power)
            except ValueError:
                print('Por favor, digite um valor válido')
                print()
            else:
                if choice_power > 0 and choice_power < 3:
                    power_name = de_encryption_power(n, choice_power)
                    v = verification(power_name)
                    if v == 'yes':
                        os.system('cls')
                        return power_name
                else:
                    ('Por favor, digite um valor válido')
                    print()

    if n == 2:
        while True:
            for x, sp in main_extra.super_power2.items():
                print(f'[{x}] : {sp}')
            choice_power = input('Faça sua escolha: ')
            try:
                choice_power = int(choice_power)
            except ValueError:
                print('Por favor, digite um valor válido')
                print()
            else:
                if choice_power > 0 and choice_power < 3:
                    power_name = de_encryption_power(n, choice_power)
                    v = verification(power_name)
                    if v == 'yes':
                        os.system('cls')
                        return power_name
                else:
                    ('Por favor, digite um valor válido')
                    print()
    if n == 3:
        while True:
            for x, sp in main_extra.super_power3.items():
                print(f'[{x}] : {sp}')
            choice_power = input('Faça sua escolha: ')
            try:
                choice_power = int(choice_power)
            except ValueError:
                print('Por favor, digite um valor válido')
                print()
            else:
                if choice_power > 0 and choice_power < 3:
                    power_name = de_encryption_power(n, choice_power)
                    v = verification(power_name)
                    if v == 'yes':
                        os.system('cls')
                        return power_name
                else:
                    ('Por favor, digite um valor válido')
                    print()
    if n == 4:
        while True:
            for x, sp in main_extra.super_power4.items():
                print(f'[{x}] : {sp}')
            choice_power = input('Faça sua escolha: ')
            try:
                choice_power = int(choice_power)
            except ValueError:
                print('Por favor, digite um valor válido')
                print()
            else:
                if choice_power > 0 and choice_power < 3:
                    power_name = de_encryption_power(n, choice_power)
                    v = verification(power_name)
                    if v == 'yes':
                        os.system('cls')
                        return power_name
                else:
                    ('Por favor, digite um valor válido')
                    print()


def de_encryption_power(n, x):
    if n == 1 and x == 1:
        power_name = list(main_extra.super_power1.values())
        return power_name[0]
    elif n == 1 and x == 2:
        power_name = list(main_extra.super_power1.values())
        return power_name[1]
    elif n == 2 and x == 1:
        power_name = list(main_extra.super_power2.values())
        return power_name[0]
    elif n == 2 and x == 2:
        power_name = list(main_extra.super_power2.values())
        return power_name[1]
    elif n == 3 and x == 1:
        power_name = list(main_extra.super_power3.values())
        return power_name[0]
    elif n == 3 and x == 2:
        power_name = list(main_extra.super_power3.values())
        return power_name[1]
    elif n == 4 and x == 1:
        power_name = list(main_extra.super_power4.values())
        return power_name[0]
    elif n == 4 and x == 2:
        power_name = list(main_extra.super_power4.values())
        return power_name[1]


def verification(x):
    verify = input(f'Você escolheu [{x}]. Tem certeza de sua escolha? (s/n): ')
    print()
    if verify.lower() == 's':
        return 'yes'


def max_dmg():
    dmg = random.randint(40, 100)
    return dmg
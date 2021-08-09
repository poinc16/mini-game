import main_extra
import os


def evilness(x):
    if x == 1:
        return 10
    elif x == 2:
        return 0


def create_character():
    your_name = name()
    your_element = choose_element()
    your_power = choose_power(your_element[0])

    your_hero = main_extra.Hero(
        your_name, your_element[1], your_power)
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
                    print('Por favor, digite um valor válido')
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


def response_choosed(decision, decision_number, branch):
    response_list = main_extra.responses.values()
    response_returned = list()
    for i in response_list:
        for j in i:
            response_returned.append(j)

    if decision_number == 1:
        if decision == 1:
            return response_returned[0]
        else:
            return response_returned[1]
    elif decision_number == 2:
        if decision == 1:
            return response_returned[2]
        else:
            return response_returned[3]
    if decision_number == 3 and branch == 1:
        if decision == 1:
            return response_returned[4]
        else:
            return response_returned[5]
    if decision_number == 3 and branch == 2:
        if decision == 1:
            return response_returned[6]
        else:
            return response_returned[7]
    if decision_number == 4 and branch == 1:
        if decision == 1:
            return response_returned[8]
        else:
            return response_returned[9]
    if decision_number == 4 and branch == 2:
        if decision == 1:
            return response_returned[10]
        else:
            return response_returned[11]
    if decision_number == 4 and branch == 3:
        if decision == 1:
            return response_returned[12]
        else:
            return response_returned[13]
    if decision_number == 4 and branch == 4:
        if decision == 1:
            return response_returned[14]
        else:
            return response_returned[15]


def verify_branch(last_decision, decision_number):
    if last_decision == 10:
        decision_value = choose_decision(decision_number, 1)
        return decision_value, 1
    elif last_decision == 0:
        decision_value = choose_decision(decision_number, 2)
        return decision_value, 2


def verify_branch_two(evil, last_branch, decision_number):
    if evil == 10:
        if last_branch == 1:
            decision_value = choose_decision(decision_number, 1)
            return decision_value, 1
        if last_branch == 2:
            decision_value = choose_decision(decision_number, 3)
            return decision_value, 3
    elif evil == 0:
        if last_branch == 1:
            decision_value = choose_decision(decision_number, 2)
            return decision_value, 2
        if last_branch == 2:
            decision_value = choose_decision(decision_number, 4)
            return decision_value, 4


def choose_decision(decision_number, branch):
    while True:
        print()
        print(f'Escolha sua  atitude ')
        x = 0
        for i in main_extra.decisions.values():
            x += 1
            for n, dc in i.items():
                if decision_number == 1 and x == 1:
                    print(f'[{n}] : {dc}')
                elif decision_number == 2 and x == 2:
                    print(f'[{n}] : {dc}')
                elif decision_number == 3 and x == 3 and branch == 1:
                    print(f'[{n}] : {dc}')
                elif decision_number == 3 and x == 4 and branch == 2:
                    print(f'[{n}] : {dc}')
                elif decision_number == 4 and x == 5 and branch == 1:
                    print(f'[{n}] : {dc}')
                elif decision_number == 4 and x == 6 and branch == 2:
                    print(f'[{n}] : {dc}')
                elif decision_number == 4 and x == 7 and branch == 3:
                    print(f'[{n}] : {dc}')
                elif decision_number == 4 and x == 8 and branch == 4:
                    print(f'[{n}] : {dc}')
        choose_decision = input('Faça sua escolha: ')

        try:
            choose_decision = int(choose_decision)
        except ValueError:
            print('Por favor, digite um valor válido!')
            print()
        else:
            if choose_decision > 0 and choose_decision < 3:
                decision_name = de_encryption_decisions(
                    choose_decision, decision_number, branch
                )
                v = verification(decision_name)
                if v == 'yes':
                    evil = evilness(choose_decision)
                    response = response_choosed(
                        choose_decision, decision_number, branch)
                    os.system('cls')
                    return decision_name, evil, response
            else:
                print('Por favor, digite um valor válido!')
                print()


def de_encryption_decisions(decision, decision_number, branch):
    decision_dict = main_extra.decisions.values()
    decision_name = list()
    for i in decision_dict:
        for j in i.values():
            decision_name.append(j)

    if decision_number == 1:
        if decision == 1:
            return decision_name[0]
        else:
            return decision_name[1]

    if decision_number == 2:
        if decision == 1:
            return decision_name[2]
        else:
            return decision_name[3]

    if decision_number == 3 and branch == 1:
        if decision == 1:
            return decision_name[4]
        else:
            return decision_name[5]

    if decision_number == 3 and branch == 2:
        if decision == 1:
            return decision_name[6]
        else:
            return decision_name[7]

    if decision_number == 4 and branch == 1:
        if decision == 1:
            return decision_name[8]
        else:
            return decision_name[9]

    if decision_number == 4 and branch == 2:
        if decision == 1:
            return decision_name[10]
        else:
            return decision_name[11]

    if decision_number == 4 and branch == 3:
        if decision == 1:
            return decision_name[12]
        else:
            return decision_name[13]

    if decision_number == 4 and branch == 4:
        if decision == 1:
            return decision_name[14]
        else:
            return decision_name[15]


def story_telling(evil, decision_number, branch):
    if evil == 10:
        if decision_number == 3:
            return 'Você sai correndo pelo lugar de onde ela veio. Ao sair da sua sala, você se depara com um cenário de completa destruição, além de perceber que o teto ainda está em desmoronamento.'
        elif decision_number == 4 and branch == 1:
            return 'Mesmo seguindo com muita calma e cuidado, um destroço grande do teto cai em cima de sua perna. Você agora está preso e com uma dor agonizante.'
        elif decision_number == 4 and branch == 2:
            return 'A pessoa se revolta e te diz que vocês são apenas um experimento de laboratório. "Você deveria estar feliz de eu ter vindo te salvar. Agora faça o que eu mando".'
    elif evil == 0:
        if decision_number == 3:
            return 'A pessoa te diz: "você agora tem poderes. Apenas os utilize para que possamos sair daqui juntos".'
        elif decision_number == 4 and branch == 1:
            return 'Você vê uma segunda saída dentro da sala em que você estava. Olhando bem dentre ela, é possível distinguir uma luz um pouco distante, parecida com a da lanterna da pessoa que te desamarrou. Instantaneamente você sai correndo naquela direção.'
        elif decision_number == 4 and branch == 2:
            return 'Ela te explica que vocês são apenas experimentos de laboratório e, através desse experimento, vocês adquiriram poderes. Ainda te diz que, para utiliza-los, basta fechar os olhos e focar todas as suas energias bem no centro do seu coração.'


def final_lore(branch, evil, power):
    if evil == 10:
        if branch == 1:
            if power == "Jato d'água":
                return main_extra.finals[0][0]
            elif power == 'Tsunami':
                return main_extra.finals[0][1]
            elif power == 'Terremoto':
                return main_extra.finals[0][2]
            elif power == 'Manipulação de rochas':
                return main_extra.finals[0][3]
            elif power == 'Lança chamas':
                return main_extra.finals[0][4]
            elif power == 'Auto combustão':
                return main_extra.finals[0][5]
            elif power == 'Furacão':
                return main_extra.finals[0][6]
            elif power == 'Vendaval':
                return main_extra.finals[0][7]
        elif branch == 2:
            return main_extra.finals[2]
        elif branch == 3:
            return main_extra.finals[4]
        elif branch == 4:
            return main_extra.finals[6]
    if evil == 0:
        if branch == 1:
            return main_extra.finals[1]
        elif branch == 2:
            return main_extra.finals[3]
        elif branch == 3:
            if power == "Jato d'água":
                return main_extra.finals[5][0]
            elif power == 'Tsunami':
                return main_extra.finals[5][1]
            elif power == 'Terremoto':
                return main_extra.finals[5][2]
            elif power == 'Manipulação de rochas':
                return main_extra.finals[5][3]
            elif power == 'Lança chamas':
                return main_extra.finals[5][4]
            elif power == 'Auto combustão':
                return main_extra.finals[5][5]
            elif power == 'Furacão':
                return main_extra.finals[5][6]
            elif power == 'Vendaval':
                return main_extra.finals[5][7]
        elif branch == 4:
            if power == "Jato d'água":
                return main_extra.finals[7][0]
            elif power == 'Tsunami':
                return main_extra.finals[7][1]
            elif power == 'Terremoto':
                return main_extra.finals[7][2]
            elif power == 'Manipulação de rochas':
                return main_extra.finals[7][3]
            elif power == 'Lança chamas':
                return main_extra.finals[7][4]
            elif power == 'Auto combustão':
                return main_extra.finals[7][5]
            elif power == 'Furacão':
                return main_extra.finals[7][6]
            elif power == 'Vendaval':
                return main_extra.finals[7][7]


def verify_evil(evil):
    return f'Seu nível de maldade, baseado em suas decisões, foi de [{evil}], sendo [40] o nível total.'

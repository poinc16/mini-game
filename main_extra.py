class Hero:
    def __init__(self, name, element, super_power, max_dmg, evil=0):
        self._super_power = super_power
        self._name = name
        self._element = element
        self._max_dmg = max_dmg
        self._evil = evil

    def decisions_choosed(choice_evil):
        number_of_decisions = list()
        number_of_decisions.append(choice_evil)
        return number_of_decisions


element = {
    '1': 'Água',
    '2': 'Terra',
    '3': 'Fogo',
    '4': 'Ar'
}

super_power1 = {
    '1': "Jato d'água",
    '2': 'Correnteza'
}

super_power2 = {
    '1': 'Jogar rochas',
    '2': 'Manipulação de rochedos menores'
}

super_power3 = {
    '1': 'Lança chamas',
    '2': 'Auto combustão'
}

super_power4 = {
    '1': 'Furacão',
    '2': 'Vendaval'
}

responses = {
    'first': [
        'Você tenta se levantar, mas está totalmente amarrado na cadeira.',
        'Você finge não estar consciente e começa a escutar a ferramenta fazer um barulho agudo e assustador.',
    ],
    'second': [
        'Você da um soco na pessoa e sai correndo por onde ela veio.',
        'Você sente seu corpo formigando por ter ficado tanto tempo amarrado. Você a vê indo embora pelo lado oposto ao que ela veio, e a segue rapidamente.',
    ],
    'third-one': [
        'Primeira ramificação primeira escolha',
        'Primeira ramificação segunda escolha'
    ],
    'third-two': [
        'Segunda ramificação primeira escolha',
        'Segunda ramificação segunda escolha'
    ]
}

decisions = {
    'first': {
        '1': 'Levantar e se defender',
        '2': 'Fingir que está inconsciente'
    },
    'second': {
        '1': 'Ataca-la e fugir',
        '2': 'Segui-la sem pestanejar',
    },
    'third-one': {
        '1': 'Primeira ramificação primeira escolha',
        '2': 'Primeira ramificação segunda escolha'
    },
    'third-two': {
        '1': 'Segunda ramificação primeira escolha',
        '2': 'Segunda ramificação segunda escolha'
    }
}

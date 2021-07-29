class Hero:
    def __init__(self, name, element, super_power, max_dmg, evil=0):
        self._super_power = super_power
        self._name = name
        self._element = element
        self._max_dmg = max_dmg
        self._evil = evil


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

first_decision = {
    '1': 'Levantar e se defender',
    '2': 'Fingir que está inconsciente',
    '3': 'Perguntar o que ele irá fazer'
}

second_decision = {
    '1': 'Ataca-la e fugir',
    '2': 'Segui-la sem pestanejar',
    '3': 'Agradeça e se junte a ela'
}

responses = {
    'first': [
        'Você tenta se levantar, mas está totalmente amarrado na cadeira.',
        'Você finge não estar consciente e começa a escutar a ferramente fazer um barulho agudo e assustador.',
        'Você tenta falar, mas não consegue.'
    ],
    'second': [
        'a',
        'b',
        'c'
    ]
}

decisions = {
    'first': {
        '1': 'Levantar e se defender',
        '2': 'Fingir que está inconsciente',
        '3': 'Perguntar o que ele irá fazer'
    },
    'second': {
        '1': 'Ataca-la e fugir',
        '2': 'Segui-la sem pestanejar',
        '3': 'Agradeça e se junte a ela'
    }
}

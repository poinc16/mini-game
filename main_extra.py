class Hero:
    def __init__(self, name, element, super_power, max_dmg):
        self._super_power = super_power
        self._name = name
        self._element = element
        self._max_dmg = max_dmg


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

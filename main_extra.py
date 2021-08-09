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
        'Você se espreguiça e agradece a ela por ter te desamarrado.',
    ],
    'third-one': [
        'Com muita cautela, você começa a seguir pelos destroços.',
        'Você vira as costas e volta para a sala. Chegando lá, percebe que a pessoa não está mais lá.'
    ],
    'third-two': [
        'Você faz uma cara de cético e diz que é impossível, pois poderes não existem.',
        'Você fica com cara de dúvida e pede explicações. A pessoa começa a falar.'
    ],
    'fourth-one': [
        'Você sente seu coração começar a ficar muito acelerado e algo estranho acontece.',
        'Você começa a gritar desesperadamente e percebe a luz da lanterna vindo em sua direção agora.'
    ],
    'fourth-two': [
        'Você tenta acertar a pessoa com uma pedra, mas acaba errando. Entretanto a pessoa percebe sua intenção e se vira para sua direção.',
        'A pessoa te escuta e fica parada esperando você chegar até ela.'
    ],
    'fourth-three': [
        'Você empurra a pessoa e ela cai no chão. Ao se levantar, é possível perceber ódio exalando dos olhos dela.',
        'Você faz um sinal de confirmação com a cabeça. Ela te explica rapidamente como utilizar seus poderes e vocês saem juntos por um corredor contrário ao que ela veio.'
    ],
    'fourth-four': [
        'A pessoa instantaneamente grita para você parar.',
        'A pessoa te da um sorriso amigo em resposta e vocês saem por um corredor contrário ao que ela veio.'
    ],
}

decisions = {
    'first': {
        '1': 'Levantar e se defender.',
        '2': 'Fingir que está inconsciente.'
    },
    'second': {
        '1': 'Ataca-la e fugir.',
        '2': 'Agradece-la e esperar as instruções.',
    },
    'third-one': {
        '1': 'Seguir por esse caminho.',
        '2': 'Voltar atrás em sua decisão, pedir desculpas para a pessoa e ver como ela pode te ajudar.'
    },
    'third-two': {
        '1': 'Duvidar do que a pessoa disse.',
        '2': 'Pedir explicações.'
    },
    'fourth-one': {
        '1': 'Fechar os olhos, respirar fundo, e fazer o máximo de força que conseguir.',
        '2': 'Gritar pedindo ajuda.'
    },
    'fourth-two': {
        '1': 'Pegar uma pedra que está no chão e jogar na pessoa.',
        '2': 'Gritar para a pessoa te esperar.'
    },
    'fourth-three': {
        '1': 'Se irritar com a maneira de falar da pessoa e confronta-la.',
        '2': 'Seguir suas ordens'
    },
    'fourth-four': {
        '1': 'Começar a canalizar o seu poder ali mesmo.',
        '2': 'Aceitar as dicas da pessoa e fugir junto dela.'
    }
}

finals = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8'
]

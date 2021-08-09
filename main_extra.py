class Hero:
    def __init__(self, name, element, super_power, evil=0):
        self._super_power = super_power
        self._name = name
        self._element = element
        self.evil = evil

    @property
    def super_power(self):
        return self._super_power

    @property
    def name(self):
        return self._name

    @property
    def element(self):
        return self._element


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
    '1': 'Terremoto',
    '2': 'Manipulação de rochas'
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
    [
        'Você começa a sentir seu corpo um pouco úmido e, repentinamente, bem do centro do seu peito, sai um jato de água muito forte que destrói o restante do teto acima, fazendo com que o restante dele caísse sobre você. VOCÊ MORREU!',
        'Você escuta um som de maré vindo de trás de você. Ao olhar para lá, é possível ver uma onda enorme vindo em sua direção. Ela passa destruindo tudo em sua volta, mas, quando te atinge, você não sente nada. Essa onda te tira de baixo dos destroços e te leva para fora do laboratório. VOCÊ SOBREVIVEU!',
        'Você sente tudo começar a tremer muito. O restante do teto começa a desabar com todos os movimentos sísmicos, e você é soterrado. VOCÊ MORREU!',
        'Você percebe que todas as rochas que estão acima de você começam a ser jogadas para longe, te deixando livre para sair dali. Por causa do seu machucado feio e da sua imensa dor, é preciso ir rastejando. Demoraram horas para que você conseguisse sair de lá, mas você conseguiu. VOCÊ SOBREVIVEU!',
        'Seu peito começa a ficar muito quente, e, bem do centro dele, sai uma labareda muito forte. Com isso, você apenas aumenta o incêndio do laboratório, fazendo com que o fogo chegue em mais substâncias químicas, que explodem o laboratório completo. VOCÊ MORREU!',
        'Você sente seu corpo inteiro começar a esquentar muito. Seu peito começa a pegar fogo e é possível ver esse fogo se espalhando pelo corpo inteiro. As rochas que estão a sua volta começam a derreter e você não sente mais dor em sua perna. Você levanta e sai correndo em direção a saída, derretendo tudo que está a sua volta. VOCÊ SOBREVIVEU!',
        'Você percebe um redemoinho começar a se formar bem no centro do seu peito. Em instanstes, aquele pequeno redemoinho se tornou um imenso furacão, que destruiu e jogou para longe de você toda a estrutura e destroços do laboratório. Assim, você consegue sair livremente por onde seria a saída quando a estrutura ainda estava lá. VOCÊ SOBREVIVEU!',
        'Você começa a sentir uma leve brisa de vento surgir atrás de você. Em poucos segundos, essa corrente de vento se tornou um vendaval fortíssimo. Através desse vendaval, o fogo se espalhou pelo restante do laboratório, fazendo com que substâncias altamente inflamáveis e explosivas recebessem o calor do incêndio. No fim, o laboratório inteiro explodiu com você dentro. VOCÊ MORREU!'
    ],
    'A pessoa olha para você, vê sua situação e te diz: "na próxima vez, não vá contra quem deu a vida para te salvar". Após terminar de falar, você vê o coração dela começar a emitir uma luz muito brilhante e, ao mesmo tempo, o resto do teto começa a desabar sobre você. VOCÊ MORREU!',
    '"Não é possível que você seja tão cretino a esse ponto!". É possível ver o coração dela brilhar e, poucos segundos depois, o você sente o chão ficar muito quente e começar a borbulhar. Pouco tempo depois disso, você é "engolido" por ele, queimando em lava. VOCÊ MORREU!',
    'Chegando nela, você pede muitas desculpas e explica que estava assustado com a situação. Ela diz que entende o seu lado e te explica que agora você possui um super-poder. Após te ensinar a utiliza-lo, vocês continuam o caminho juntos. VOCÊ SOBREVIVEU!',
    '"Eu só estava tentando te ajudar, mas já que você quer assim... assim será!". É possível ver o coração dela começar a acelerar muito os batimentos e, instantaneamente depois, você é atingido por trás por uma imensa onda de água que te leva em direção a parede. Com a força que a água te jogou e seu impacto na parede, a mesma desmorona em cima de você. VOCÊ MORREU!',
    [
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Com os jatos de água que você solta, você consegue ir destruindo os destroços que vão caindo sobre vocês, até que chegam no final e conseguem sair. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você faz uma onda gigantesca atrás de vocês, que leva vocês dois para o final do corredor em segurança. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você cria um terremoto, tentando fazer com que abrisse caminho pelo solo para vocês passarem, mas não dá certo. Isso apenas acelera a velocidade de destruição do laboratório e vocês são soterrados. VOCÊ MORREU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você começa a controlar as rochas que caem do teto e joga-las para longe. Vocês chegam, com facilidade, no final do corredor. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali e começa a utilizar o lança chamas que você cria no peito para tentar ir derretendo as rochas que caem do teto. Porém, isso não dá certo e vocês acabam sendo soterrados. VOCÊ MORREU',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você deixa seu corpo inteiro em combustão, fazendo com que derretesse qualquer coisa que encostasse. Com isso, você abriu espaço por outro local do corredor e vocês conseguiram sair de lá. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você cria um imenso furacão que destrói o restante da estrutura do laboratório, e jogando para longe toda a estrutura dele. Assim, vocês tiveram caminho livre para irem embora. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você faz com que o vendaval carregasse as rochas que cairiam sobre vocês para longe. Sendo assim, vocês conseguem sair de lá com facilidade. VOCÊ SOBREVIVEU!'
    ],
    '"Não faça isso! Se você sair utilizando seus poderes assim, vai acabar matando nós dois!", porém você não consegue controlar a canalização de suas energias. É possível sentir seu coração acelerando muito e começando a brilhar. Como um ato final de desespero, a pessoa tira a faca, que utilizou para cortar suas amarras, do bolso e enfia diretamente no seu coração. VOCÊ MORREU!',
    [
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Com os jatos de água que você solta, você consegue ir destruindo os destroços que vão caindo sobre vocês, até que chegam no final e conseguem sair. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você faz uma onda gigantesca atrás de vocês, que leva vocês dois para o final do corredor em segurança. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você cria um terremoto, tentando fazer com que abrisse caminho pelo solo para vocês passarem, mas não dá certo. Isso apenas acelera a velocidade de destruição do laboratório e vocês são soterrados. VOCÊ MORREU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você começa a controlar as rochas que caem do teto e joga-las para longe. Vocês chegam, com facilidade, no final do corredor. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali e começa a utilizar o lança chamas que você cria no peito para tentar ir derretendo as rochas que caem do teto. Porém, isso não dá certo e vocês acabam sendo soterrados. VOCÊ MORREU',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você deixa seu corpo inteiro em combustão, fazendo com que derretesse qualquer coisa que encostasse. Com isso, você abriu espaço por outro local do corredor e vocês conseguiram sair de lá. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você cria um imenso furacão que destrói o restante da estrutura do laboratório, e jogando para longe toda a estrutura dele. Assim, vocês tiveram caminho livre para irem embora. VOCÊ SOBREVIVEU!',
        'Durante o caminho, você percebe que o restante do laboratório está desabando sobre vocês. Você percebe que a pessoa, através de seu poder, fez um grande escudo de pedra acima de vocês dois, porém percebe que ele não irá durar muito tempo. Você decide, então, utilizar seu poder para conseguirem sair dali. Você faz com que o vendaval carregasse as rochas que cairiam sobre vocês para longe. Sendo assim, vocês conseguem sair de lá com facilidade. VOCÊ SOBREVIVEU!'
    ]
]

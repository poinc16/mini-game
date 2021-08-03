import func

clear_page = func.os

# Primeira parte -> criação do personagem
print('Você acorda em um local estranho, parecido com um laboratório, cheio de bugigangas. Ao olhar para o lado, você vê um homem com um avental branco e cara de maluco vindo até você. Ele te olha com uma cara alegre, como se estivesse surpreso por você ter acordado.')

char1 = func.create_character()

print(f'Seu nome é: {char1._name}')
print(f'Seu elemento é: {char1._element}')
print(f'Seu poder é: {char1._super_power}')
print(f'O dano do seu poder é: {char1._max_dmg}')
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Segunda parte -> "personagem perde a consciência"
print('Ao olhar para o possível cientista, você percebe que ele está vindo em sua direção com uma ferramenta parecida com uma furadeira. É também possível perceber que ele não olha para seu rosto em si, e sim para a uma região específica da sua cabeça.')

decision1 = func.choose_decision(1)
# char1.decisions_choosed(pass)
char1._evil += decision1[1]

print(decision1[2])
print()
print('Você escuta a ferramenta começar a perfurar a sua cabeça, mas não sente nada. Começa a escutar uma risada de fundo e, repentinamente, sua mente desliga como se fosse uma televisão.')
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Terceira parte -> personagem tem sua primeira interação com o "mundo novo"
print('Quando você acorda e olha para os lados, percebe que o antigo laboratório está completamente destruído. Todos os mecanismos estão pegando fogo, algumas partes do teto estão desmoronando e você percebe o sinal de alerta piscando freneticamente. Seus ouvidos parecem estar entupidos, pois ouve os sons baixos e relativamente distantes.')
print()
print('Da porta em frente a sua "maca", é possível perceber um luz meio rosa vindo em sua direção. É como se alguma pessoa estivesse utilizando algum traje específico que emana essa luminescência. Ela vem em sua direção e solta suas amarras rapidamente, sem nem olhar para o seu rosto.')

decision2 = func.choose_decision(2)
# char1.decisions_choosed(evilness[1])
char1._evil += decision2[1]

print(decision2[2])
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Quarta parte -> começa agora as ramificações da história, baseadas em usas escolhas
print('#####################################')

decision3 = func.choose_decision(3)
# char1.decisions_choosed(evilness[2])
char1._evil += decision3[1]

print(decision3[2])
input('Press [ENTER] to continue!')

input('Press [ENTER] to end-Game!')

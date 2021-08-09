import func

clear_page = func.os

# Primeira parte -> criação do personagem
print('Você acorda em um local estranho, parecido com um laboratório, cheio de bugigangas. Ao olhar para o lado, você vê um homem com um avental branco e cara de maluco vindo até você. Ele te olha com uma cara alegre, como se estivesse surpreso por você ter acordado.')

char1 = func.create_character()

print(f'Seu nome é: {char1.name}')
print(f'Seu elemento é: {char1.element}')
print(f'Seu poder é: {char1.super_power}')
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Segunda parte -> "personagem perde a consciência"
print('Ao olhar para o possível cientista, você percebe que ele está vindo em sua direção com uma ferramenta parecida com uma furadeira. É também possível perceber que ele não olha para seu rosto em si, e sim para a uma região específica da sua cabeça.')

decision1 = func.choose_decision(1, 0)
char1.evil += decision1[1]

print(decision1[2])
print()
print('Você escuta a ferramenta começar a perfurar a sua cabeça, mas não sente nada. Começa a escutar uma risada de fundo e, repentinamente, sua mente desliga como se fosse uma televisão.')
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Terceira parte -> personagem tem sua primeira interação com o "mundo novo"
print('Quando você acorda e olha para os lados, percebe que o antigo laboratório está completamente destruído. Todos os mecanismos estão pegando fogo, algumas partes do teto estão desmoronando e você percebe o sinal de alerta piscando freneticamente. Seus ouvidos parecem estar entupidos, pois ouve os sons baixos e relativamente distantes.')
print()
print('Da porta em frente a sua "maca", é possível perceber uma luz vindo em sua direção. É como se alguma pessoa estivesse vindo até você com uma lanterna apontada para sua direção. Ela vem em sua direção e solta suas amarras rapidamente, sem nem olhar para o seu rosto.')

decision2 = func.verify_branch(decision1[1], 2)
char1.evil += decision2[0][1]

print(decision2[0][2])
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Quarta parte -> começa agora as ramificações da história, baseadas em usas escolhas
print(func.story_telling(decision2[0][1], 3, decision2[1]))

decision3 = (func.verify_branch(decision2[0][1], 3))
char1.evil += decision3[0][1]

print(decision3[0][2])
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Quinta parte -> decisão final
print(func.story_telling(decision3[0][1], 4, decision3[1]))

decision4 = func.verify_branch_two(decision3[0][1], decision3[1], 4)
char1.evil += decision4[0][1]


print(decision4[0][2])
input('Press [ENTER] to continue!')

clear_page.system('cls')

# Sexta parte -> final (possuindo vários finais diferentes)
print(func.final_lore(decision4[1], decision4[0][1], char1.super_power))
print()
print('###########################################################################')
print(func.verify_evil(char1.evil))
print()
input('Press [ENTER] to end-Game!')

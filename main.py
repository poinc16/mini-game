import func
imported = func.main_extra
clear_page = func.os

print('Você acorda em um local estranho, parecido com um laboratório, cheio de bugigangas. Ao olhar para o lado, você vê um homem com um avental branco e cara de maluco vindo até você. Ele te olha com uma cara alegre, como se estivesse surpreso por você ter acordado.')
char1 = func.create_character()
print(f'Seu nome é: {char1._name}')
print(f'Seu elemento é: {char1._element}')
print(f'Seu poder é: {char1._super_power}')
print(f'O dano do seu poder é: {char1._max_dmg}')
press_continue = input('Press [ENTER] to continue!')

clear_page.system('cls')

print('Ao olhar para o possível cientista, você percebe que ele está vindo em sua direção com uma ferramenta parecida com uma furadeira. É também possível perceber que ele não olha para seu rosto em si, e sim para a uma região específica da sua cabeça.')
decision1 = func.choose_first_decision()
char1._evil += decision1[1]
print(decision1[2])

input('Press [ENTER] to end-Game!')

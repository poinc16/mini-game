import func
imported = func.main_extra

print('Você acorda em um local estranho, parecido com um laboratório, cheio de bugigangas. Ao olhar para o lado, você vê um homem com um avental branco e cara de maluco vindo até você. Ele te olha com uma cara alegre, como se estivesse surpreso por você ter acordado.')

hero1 = func.create_character()

print(f'Seu nome é: {hero1._name}')
print(f'Seu elemento é: {hero1._element}')
print(f'Seu poder é: {hero1._super_power}')
print(f'O dano do seu poder é: {hero1._max_dmg}')

input('Press [ENTER] to end-Game!')

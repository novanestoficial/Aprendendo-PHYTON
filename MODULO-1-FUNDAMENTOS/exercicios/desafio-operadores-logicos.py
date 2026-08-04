# TERCA E QUITA( TRUE OR FALSE)




# se apenas um trabalho der certo a pessoa leva uma tv de 32

#se os DOIS der certo a pessoa leva uma tv de 50 polegadas


#se um dos dois cenarios der certo a familia vai tomar sorvete pra comemorar

# se nenhum der certo todos ficam com + saude 




# trabalho_terca = input("O trabalho de terça deu certo? [S/N]: ").upper() == "S"
# trabalho_quinta = input("O trabalho de quinta deu certo? [S/N]: ").upper() == "S"

# if trabalho_terca and trabalho_quinta:
    # print("Voce levou uma tv de 50 polegadas e tomou sorvete com a sua familia")
# elif trabalho_terca or trabalho_quinta:
    # print("Voce levou uma tv de 32 polegadas e tomou sorvete com a sua familia")
# else:
    # print("Voces ficaram com saude e nao tomaram nada!")  



trabalho_terca = True
trabalho_quinta = False


tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
saudavel = not sorvete
print("TV50 = {} TV32 = {} Sorvete = {} Saudavel = {}".format(tv_50, sorvete, tv_32, saudavel))

    




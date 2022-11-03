import random
f = open('puntaje.txt','a',encoding='utf8')
for _ in range(1,4):
    user_action=input("seleccione piedra-papel-tijera)")
    possible_actions= ["piedra","papel","tijera"]
    computer_action=random.choice(possible_actions)
 #   print(computer_action)
    print("\nTú elegiste : ", user_action , " , La computadora eligió : ", computer_action)
    if user_action == computer_action:
        print("Empate !" ,user_action, ", Ambos ganaron !")
        f.write("empate. \n")
    elif user_action=="piedra" and computer_action=="papel":
        print("Ganó la computadora ! . \n")
        f.write("Ganó la computadora. \n")
    elif user_action=="piedra" and computer_action=="tijera":
        print("Ganó el usuario ! . \n")
        f.write("Ganó el usuario. \n")
    elif user_action=="papel" and computer_action=="piedra":
        print("Ganó el usuario ! . \n")
        f.write("Ganó el usuario. \n")
    elif user_action=="papel" and computer_action=="tijera":
        print("Ganó la computadora ! . \n")
        f.write("Ganó la computadora. \n")
    elif user_action=="tijera" and computer_action=="piedra":
        print("Ganó el usuario ! . \n")
        f.write("Ganó el usuario. \n")
    elif user_action=="tijera" and computer_action=="papel":
        print("Ganó la computadora ! . \n")
        f.write("Ganó la computadora. \n")
    else:
        print("Error seleccione correctamente !")
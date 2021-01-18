import random

while True:
    bullet_position = 2


    def fire_gun():
        camber_position = random.randint(1, 6)
        print(camber_position)
        if camber_position == bullet_position:
            print("you are dead!")
        else:
            print("keep playing!")

    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        fire_gun()
    else:
        break


print(fire_gun())

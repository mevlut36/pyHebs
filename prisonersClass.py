import time

import yaml


def rebellion():
    with open("data/data.yml") as file:
        data = yaml.safe_load(file)
    timer = 15
    print("REBELLION : The prisoners are not happy. The guards will try to manage it.")
    while True:
        timer -= 1
        print(str(timer) + " before the end...")
        time.sleep(1)
        gardiens = data["prison"]["gardiens"]
        detenus = data["prison"]["detenus"]
        protection = data["prison"]["protection-gardien"]
        if gardiens + protection > detenus:
            detenus -= detenus
        else:
            gardiens -= gardiens

        if timer == 0:
            if gardiens > detenus:
                return "The rebellion has ended. The rebellion was successfully managed"
            else:
                return "The prison is in the hands of the prisoners, You lose."


def moodPrisoners():
    with open("data/data.yml") as file:
        data = yaml.safe_load(file)
    calcul = data["prison"]["cuisine-level"] + \
             data["prison"]["cellule-level"] + \
             data["prison"]["cour-prison"] + \
             data["prison"]["infirmerie-level"]
    mood = data["prison"]["detenus"] / calcul ** 2
    if mood > 0.5:
        print(rebellion())
    return mood


print(moodPrisoners())

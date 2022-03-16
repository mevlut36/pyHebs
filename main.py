import os
import time
import yaml
from yaml import Loader
import threading

running = True
hour, minute, seconds = 11, 30, 0

impot = 160
revenue_par_detenus = 80

src_data = "data/data.yml"


def mevTimer():
    file = open(src_data, 'r')
    data = yaml.load(file, Loader=Loader)
    while True:
        data['time']['seconds'] += 1
        time.sleep(0.10)
        with open(src_data, 'w') as yaml_file:
            yaml_file.write(yaml.dump(data))
        if data['time']['seconds'] > 59:
            data['time']['minute'] += 1
            data['time']['seconds'] = 0
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
        elif data['time']['minute'] > 59:
            data['time']['hour'] += 1
            data['time']['minute'] = 0
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
        elif data['time']['hour'] > 23:
            data['time']['hour'] = 0
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
        time.sleep(60)
        # print('[' + str(hour) + ':' + str(minute) + ']')


def routine():
    if hour == 12:
        return "Midi"
    elif hour == 7:
        return "Debut de la matiné"
    elif hour == 19 and minute == 30:
        return "Diner"
    elif hour == 0:
        return "Bonne nuit"
    else:
        return "Libre"


def getDataYML(key, value):
    with open("data/data.yml") as file:
        data = yaml.safe_load(file)
        return data[key][value]


def pay(price):
    file = open(src_data, 'r')
    data = yaml.load(file, Loader=Loader)
    data['resources']['money'] -= price
    with open(src_data, 'w') as yaml_file:
        yaml_file.write(yaml.dump(data))


def earn(price):
    file = open(src_data, 'r')
    data = yaml.load(file, Loader=Loader)
    data['resources']['money'] += price
    with open(src_data, 'w') as yaml_file:
        yaml_file.write(yaml.dump(data))


def getResources():
    a = input("Que voulez-vous savoir ? (Eau = 1 / Elec = 2 / Argent = 3)")
    if a == "1" or a == "Eau":
        return "Litre d'eau: " + str(getDataYML('resources', "water")) + "L"

    elif a == "2" or a == "Elec":
        return "Electricité: " + str(getDataYML('resources', "volt")) + "V"

    elif a == "Argent" or a == "3":
        return "Mon argent:" + str(getDataYML('resources', "money")) + "€"


def getInfoPrison():
    a = input("Que voulez-vous savoir ? (Nb de prisoniers = 1 / cellules total = 2)")
    if a == '1':
        return "Nombre de prisonniers: " + str(getDataYML('prison', 'detenus'))
    elif a == '2':
        return "Cellules total: " + str(getDataYML('prison', 'cellules')) \
               + '/' + \
               str(getDataYML('prison', 'max-cellules'))


def upgradePrison():
    a = input("Que souhaitez-vous améliorer ? (Ajouter une cellule = 1 / Infirmerie = 2 / Sanitaire = 3)")
    if a == "1":
        ab = input("Quel cellule ? ({0})".format(str(getDataYML('prison', 'cellules'))))
        if ab == str(getDataYML('prison', 'cellules')):
            abc = input(f"Le prix est de 10€. Vous avez {str(getDataYML('resources', 'money'))}€,"
                        f"souhaitez vous l'améliorer ? (y/n)")
            if abc == "y" or abc == "yes":
                pay(10)


def helpCmd():
    return "--->Commands list<--- \n" \
           "/resources | /res | /rs : Check your resources \n" \
           "/help : Check commands list \n" \
           "/infoprison | /ip : Check information about your prison \n" \
           "/up-prison : Upgrade something about your prison \n" \
           "<------------------->"


def init_yml():
    if os.path.getsize("data/data.yml") == 0:
        f = open("data/data.yml", "a")
        f.write("resources:\n"
                "   money: 2000\n"
                "   water: 100\n"
                "   volt: 120\n"
                "prison:\n"
                "   detenus: 2\n"
                "   gardiens: 5\n"
                "   cuisinier: 2\n"
                "   agent: 3\n"
                "   cellules: 1\n"
                "   max-cellules: 8\n")
        return "YML file created"


if __name__ == '__main__':
    timer_thread = threading.Thread(target=mevTimer)
    timer_thread.start()
    if os.path.getsize("data/data.yml") == 0:
        print(init_yml())
    else:
        print("YML file loaded")
    while running:
        cmd = input(str(getDataYML('resources', "money")) + "€ | " + str(getDataYML('resources', "water")) + "L | "
                    + str(getDataYML('resources', "volt")) + "V | [" + str(getDataYML('time', 'hour')) + ":"
                    + str(getDataYML('time', 'minute')) + "] |" + routine() + "|" + " #>")
        if cmd == "/res" or cmd == "/resources" or cmd == "/rs":
            print(getResources())
        if cmd == "/help":
            print(helpCmd())
        if cmd == "/infoprison" or cmd == "/ip":
            print(getInfoPrison())
        if cmd == "/up-prison" or cmd == "/up":
            print(upgradePrison())

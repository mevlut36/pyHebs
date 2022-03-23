import os
import time
import yaml
from yaml import Loader
import threading
import ClassPrison
from TextFormat import textColor

running = True


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

impot = 160
revenue_par_detenus = 80 * int(getDataYML('prison', 'detenus'))


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
            data['resources']['money'] += revenue_par_detenus
            print(textColor.GREEN + "Vous avez gagner " + str(revenue_par_detenus) + "€" + textColor.END)
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
        elif data['time']['hour'] > 23:
            data['time']['hour'] = 0
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
        time.sleep(60)
        # print('[' + str(hour) + ':' + str(minute) + ']')


def routine():
    file = open(src_data, 'r')
    data = yaml.load(file, Loader=Loader)
    if 12 <= data['time']['hour'] <= 13:
        return "Midi"
    elif 7 <= data['time']['hour'] <= 8:
        return "Debut de la matiné"
    elif 19 <= data['time']['hour'] <= 20:
        return "Diner"
    elif data['time']['hour'] > 23:
        return "Bonne nuit"
    else:
        return "Libre"


def getResources():
    return textColor.BLUE + "Litre d'eau: " + str(getDataYML('resources', "water")) + "L \n" + \
           textColor.YELLOW + "Electricité: " + str(getDataYML('resources', "volt")) + "V \n" + \
           textColor.GREEN + "Mon argent: " + str(getDataYML('resources', "money")) + "€" + textColor.END


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
        if getDataYML('prison', 'cellules') > getDataYML('prison', 'max-cellules'):
            abc = input(f"Le prix est de 10€. Vous avez {str(getDataYML('resources', 'money'))}€,"
                        f"souhaitez vous l'améliorer ? (y/n)")
            if abc == "y" or abc == "yes":
                prison = ClassPrison.Prison()
                prison.addCellule(1000)
                return "Amélioration effectuer"
        else:
            return textColor.RED + "Vous avez atteint le nombre maximal de cellules dans cette prison." + textColor.END


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
                "   max-cellules: 8\n"
                "time:\n"
                "   hour: 20\n"
                "   minute: 31\n"
                "   seconds: 0\n")
        return textColor.YELLOW + "Warning : No YML files were found. New file created." + textColor.END


if __name__ == '__main__':
    if os.path.getsize("data/data.yml") == 0:
        print(init_yml())
    while running:
        timer_thread = threading.Thread(target=mevTimer)
        timer_thread.start()
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
        else:
            print(textColor.HEADER + "Command not found, try /help" + textColor.END)

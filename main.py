import os
import yaml
from yaml import Loader
import threading
import ClassPrison
from TextFormat import textColor
from Time import Time

running = True


def init_yml():
    if os.path.getsize("data/data.yml") == 0:
        f = open("data/data.yml", "a")
        f.write("prison:\n"
                "   agents: 3\n"
                "   cellule-level: 1\n"
                "   cellule-level-max: 1\n"
                "   cellules: 7\n"
                "   cour-prison: 1\n"
                "   cour-prison-max: 1\n"
                "   cuisine-level: 1\n"
                "   cuisine-level-max: 1\n"
                "   cuisiniers: 2\n"
                "   detenus: 2\n"
                "   gardiens: 3\n"
                "   generateur-level: 1\n"
                "   generateur-level-max: 1\n"
                "   infirmerie-level: 1\n"
                "   infirmerie-level-max: 1\n"
                "   max-agents: 6\n"
                "   max-cellules: 8\n"
                "   max-cuisiniers: 8\n"
                "   max-gardiens: 20\n"
                "   pompe-eau-level: 1\n"
                "   pompe-eau-level-max: 1\n"
                "   protection-gardien: 1\n"
                "   protection-gardien-max: 1\n"
                "resources:\n"
                "   money: 18470\n"
                "   volt: 120\n"
                "   water: 100\n"
                "time:\n"
                "   hour: 12\n"
                "   minute: 0\n"
                "   seconds: 34\n")
        return textColor.YELLOW + "Warning : No YML files were found. New file created." + textColor.END

if os.path.getsize("data/data.yml") == 0:
    print(init_yml())


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


if __name__ == '__main__':
    while running:
        timer_thread = threading.Thread(target=Time.mevTimer)
        timer_thread.start()
        cmd = input(str(getDataYML('resources', "money")) + "€ | " + str(getDataYML('resources', "water")) + "L | "
                    + str(getDataYML('resources', "volt")) + "V | [" + str(getDataYML('time', 'hour')) + ":"
                    + str(getDataYML('time', 'minute')) + "] |" + Time.routine() + "|" + " #>")
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

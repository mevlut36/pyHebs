import time
import yaml
import threading

running = True
hour = 11
minute = 30
seconds = 0

impot = 160
revenue_par_detenus = 80


def mevTimer():
    global seconds
    global minute
    global hour
    while True:
        seconds += 1
        time.sleep(0.10)
        if seconds > 59:
            minute += 1
            seconds = 0
        elif minute > 59:
            hour += 1
            minute = 0
        elif hour > 23:
            hour = 0
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
    with open("data/data.yml", "w") as file:
        data = yaml.safe_load(file)
        return data["resources"]["money"] - price


def earn(price):
    with open("data/data.yml", "w") as file:
        data = yaml.safe_load(file)
        return data["resources"]["money"] + price


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
        return "Cellules total: " + str(getDataYML('prison', 'cellules'))\
               + '/' +\
               str(getDataYML('prison', 'max-cellules'))


def upgradePrison():
    a = input("Que souhaitez-vous améliorer ? (Ajouter une cellule = 1 / Infirmerie = 2 / Sanitaire = 3)")
    if a == "1":
        ab = input("Quel cellule ? ({0})".format(str(getDataYML('prison', 'cellules'))))
        if ab == "1":
            abc = "Le prix est de 10€. Vous avez {0}, souhaitez vous l'améliorer ? (y/n)"
            if abc == "y" or abc == "yes":
                pay(10)


def helpCmd():
    return "--->Commands list<--- \n" \
           "/resources | /res | /rs : Check your resources \n" \
           "/help : Check commands list \n" \
           "/infoprison | /ip : Check information about your prison \n" \
           "/up-prison : Upgrade something about your prison \n" \
           "<------------------->"


if __name__ == '__main__':
    timer_thread = threading.Thread(target=mevTimer)
    timer_thread.start()
    while running:
        cmd = input(str(getDataYML('resources', "money")) + "€ | " + str(getDataYML('resources', "water")) + "L | "
                    + str(getDataYML('resources', "volt")) + "V | [" + str(hour) + ":" + str(minute) + "] |" + routine() + "|" + " #>")
        if cmd == "/res" or cmd == "/resources" or cmd == "/rs":
            print(getResources())
        if cmd == "/help":
            print(helpCmd())
        if cmd == "/infoprison" or cmd == "/ip":
            print(getInfoPrison())

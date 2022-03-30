from main import getDataYML, upgradePrison
import yaml
from yaml import Loader

src_data = "data/data.yml"


class Prison:
    def __init__(self):
        pass

    def addCellule(self, price):
        if getDataYML("prison", "cellules") < getDataYML("prison", "max-cellules"):
            if getDataYML("resources", "money") >= price:
                file = open(src_data, 'r')
                data = yaml.load(file, Loader=Loader)
                data['resources']['money'] -= price
                data['prison']['cellules'] += 1
                with open(src_data, 'w') as yaml_file:
                    yaml_file.write(yaml.dump(data))
                return "Cell added."
            else:
                return "You don't have enough money."
        else:
            return "You have built enough cells."

    def addGardien(self, price):
        if getDataYML("prison", "gardiens") < getDataYML("prison", "max-gardiens"):
            if getDataYML("resources", "money") >= price:
                file = open(src_data, 'r')
                data = yaml.load(file, Loader=Loader)
                data['resources']['money'] -= price
                data['prison']['gardiens'] += 1
                with open(src_data, 'w') as yaml_file:
                    yaml_file.write(yaml.dump(data))
                return "Guard hired."
            else:
                return "You don't have enough money."
        else:
            return "You have enough guard."

    def addCuisinier(self, price):
        if getDataYML("prison", "cuisiniers") < getDataYML("prison", "max-cuisiniers"):
            if getDataYML("resources", "money") >= price:
                file = open(src_data, 'r')
                data = yaml.load(file, Loader=Loader)
                data['resources']['money'] -= price
                data['prison']['cuisiniers'] += 1
                with open(src_data, 'w') as yaml_file:
                    yaml_file.write(yaml.dump(data))
                return "chef hired."
            else:
                return "You don't have enough money."
        else:
            return "You have enough chef."

    def addAgent(self, price):
        if getDataYML("prison", "agents") < getDataYML("prison", "max-agents"):
            if getDataYML("resources", "money") >= price:
                file = open(src_data, 'r')
                data = yaml.load(file, Loader=Loader)
                data['resources']['money'] -= price
                data['prison']['agents'] += 1
                with open(src_data, 'w') as yaml_file:
                    yaml_file.write(yaml.dump(data))
                return "cleaner hired."
            else:
                return "You don't have enough money."
        else:
            return "You have enough cleaner."

    def removeGardien(self):
        if getDataYML("prison", "gardiens") > 0:
            file = open(src_data, 'r')
            data = yaml.load(file, Loader=Loader)
            data['prison']['gardiens'] -= 1
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
            return "Guard lay off."
        else:
            return "You don't have guard for lay off"

    def removeCuisinier(self):
        if getDataYML("prison", "cuisiniers") > 0:
            file = open(src_data, 'r')
            data = yaml.load(file, Loader=Loader)
            data['prison']['cuisiniers'] -= 1
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
            return "Chef lay off."
        else:
            return "You don't have chef for lay off"

    def removeAgent(self):
        if getDataYML("prison", "agents") > 0:
            file = open(src_data, 'r')
            data = yaml.load(file, Loader=Loader)
            data['prison']['agents'] -= 1
            with open(src_data, 'w') as yaml_file:
                yaml_file.write(yaml.dump(data))
            return "Cleaner lay off."
        else:
            return "You don't have cleaner for lay off"

    def upgradePrison(self, element, price):
        if element == "cellule":
            if getDataYML("prison", "cellule-level") < getDataYML("prison", "cellule-level-max"):
                if getDataYML("resources", "money") >= price:
                    file = open(src_data, 'r')
                    data = yaml.load(file, Loader=Loader)
                    data['resources']['money'] -= price
                    data['prison']['cellule-level'] += 1
                    with open(src_data, 'w') as yaml_file:
                        yaml_file.write(yaml.dump(data))
                    return "Cell upgraded."
                else:
                    return "You don't have enough money."
            else:
                return "You have reached the maximum level of the cells."

        if element == "cuisine":
            if getDataYML("prison", "cuisine-level") < getDataYML("prison", "cuisine-level-max"):
                if getDataYML("resources", "money") >= price:
                    file = open(src_data, 'r')
                    data = yaml.load(file, Loader=Loader)
                    data['resources']['money'] -= price
                    data['prison']['cuisine-level'] += 1
                    with open(src_data, 'w') as yaml_file:
                        yaml_file.write(yaml.dump(data))
                    return "Kitchen upgraded."
                else:
                    return "You don't have enough money."
            else:
                return "You have reached the maximum level of the kitchen."

import time
import yaml
from yaml import Loader

import main
from TextFormat import textColor
src_data = "data/data.yml"


class Time:

    def __init__(self):
        pass

    @staticmethod
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
                data['resources']['money'] += main.revenue_par_detenus
                print(textColor.GREEN + "Vous avez gagner " + str(main.revenue_par_detenus) + "€" + textColor.END)
                with open(src_data, 'w') as yaml_file:
                    yaml_file.write(yaml.dump(data))
            elif data['time']['hour'] > 23:
                data['time']['hour'] = 0
                with open(src_data, 'w') as yaml_file:
                    yaml_file.write(yaml.dump(data))
            time.sleep(60)

    @staticmethod
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

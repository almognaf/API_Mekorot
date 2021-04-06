import json


defaultConfigData = {
        "key": "", #you need to put here a default session key
        "mekorotUrl": "https://mekorot.realiteq.net/",
        "dataFolderPath": "Data",
        "periodInSec": "3600",
        "intervalOfSamplesInSec": "60",
        "subnodesDepth": "20",
        "lastUpdate": "none"
}


def read_json_file(file_name):
    with open(file_name) as json_file:
        return json.load(json_file)


class Config:
    @staticmethod
    def load_config_file():
        config = read_json_file('config.json')
        if config is None:
            print("Config file not found!\nCreates default file:")
            with open('config.json', 'w') as outfile:
                json.dump(defaultConfigData, outfile)
            config = read_json_file('config.json')
        return config

    @staticmethod
    def get_lastUpdate_from_config():
        return Config.load_config_file()['lastUpdate']


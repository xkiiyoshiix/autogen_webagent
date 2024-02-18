import json


class Json():
    def __init__(self) -> None:
        pass

    def readConfig(self, file_name, key):
        with open(file_name) as file:
            config = json.load(file)

        value = config[key]
        return value
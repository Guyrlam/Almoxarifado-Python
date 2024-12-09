import json
import os


class DataBase:

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump({}, file)

        with open(file_path, "r") as file:
            self.data = json.load(file)

    @staticmethod
    def save(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file)

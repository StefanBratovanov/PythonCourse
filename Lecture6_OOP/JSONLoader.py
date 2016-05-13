from Loader import Loader
import json


class JSONLoader(Loader):
    def __init__(self, filename):
        super().__init__(filename)

    def load(self):
        with open(input_filename) as f:
            input_data = json.load(f)
            return input_data

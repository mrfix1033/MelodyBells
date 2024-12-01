from mrfix1033.melodybells.data.File import File
import yaml

from mrfix1033.melodybells.utils import Constants


class YamlFile(File, dict):
    def __init__(self, path):
        super().__init__(path)
        self.__dict__.update()

    def _load(self):
        with open(self.path, encoding=Constants.file_encoding) as file:
            self.data = yaml.safe_load(file)
            print(self.data)  # todo remove
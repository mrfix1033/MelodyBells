from mrfix1033.melodybells.data.YamlFile import YamlFile


class Config(YamlFile):
    def __init__(self, path):
        super().__init__(path)
        self.language =
        self._load()
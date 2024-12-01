from mrfix1033.melodybells.data.YamlFile import YamlFile
import yaml


class I18N:
    def __init__(self, yaml_file: YamlFile):
        with yaml_file.open() as stream:
            yml = yaml.safe_load(stream)
        self.select_audio = yml["select_audio"]


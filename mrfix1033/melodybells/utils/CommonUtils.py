import locale
import ctypes
import os.path

from mrfix1033.melodybells.data.YamlFile import YamlFile
from mrfix1033.melodybells.exceptions.LocalizationNotFoundError import LocalizationNotFoundError
from mrfix1033.melodybells.i18n.I18N import I18N
from mrfix1033.melodybells.utils.Constants import *


def get_system_language():
    windll = ctypes.windll.kernel32
    os_language = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # todo check on linux
    return os_language#.lower()


def is_file_or_dir_exists(path):
    return os.path.exists(path)


def get_default_language():
    return "en_en"


def load_localization():
    language = get_system_language()
    localization_file_path = localization_folder + language + yml_extension
    if not is_file_or_dir_exists(localization_file_path):
        language = get_default_language()
        localization_file_path = localization_folder + language + yml_extension
        if not is_file_or_dir_exists(localization_file_path):
            raise LocalizationNotFoundError("")
    localization_file = YamlFile(localization_file_path)
    localization = I18N(localization_file)
    return localization

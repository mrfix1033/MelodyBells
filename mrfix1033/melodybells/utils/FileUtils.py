import os.path
import locale
import ctypes

from mrfix1033.melodybells.data.YamlFile import YamlFile
from mrfix1033.melodybells.exceptions.localization import LocalizationNotFoundError
from mrfix1033.melodybells.i18n.I18N import I18N
from mrfix1033.melodybells.utils import Constants
from mrfix1033.melodybells.utils.Constants import *


def get_system_locale():
    windll = ctypes.windll.kernel32
    os_language = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # todo check on linux
    return os_language


def is_file_or_dir_exists(path):
    return os.path.exists(path)

def make_dirs(dirs):
    os.makedirs(dirs, exist_ok=True)

def get_locale(configLocale) -> tuple[str, str]:
    """
    :param configLocale: Locale from the config, specify None to ignore
    :return: a tuple of 2 elements: the name of the locale, the path to the localization file
    """
    locales = get_system_locale(), Constants.default_locale
    if configLocale is not None:
        locales = (configLocale,) + locales
    for tryingLocale in locales:
        localization_file_path = localization_folder + tryingLocale + yml_extension
        if is_file_or_dir_exists(localization_file_path):
            break
    else:
        raise LocalizationNotFoundError(Messages.none_of_localizations_were_found % ', '.join(locales))
    return tryingLocale, localization_file_path

def load_localization(configLocale):
    make_dirs(localization_folder)
    localization_file_path = get_locale(configLocale)[1]
    localization_file = YamlFile(localization_file_path)
    localization = I18N(localization_file)
    return localization
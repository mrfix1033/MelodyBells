class MelodyBells:
    def __init__(self):
        ProgramUtils.create_files()

        self.localization = CommonUtils.load_localization()

        self.logger = Logger(Constants.log_file)

        self.error_utils = ErrorUtils(self.localization, self.logger)
        self.error_utils.register()

        self.main_window = MainWindow(self)


if __name__ == "__main__":
    import sys

    from PyQt5 import QtWidgets, QtCore, QtGui
    from PyQt5.QtWidgets import QApplication

    from mrfix1033.melodybells.data.YamlFile import YamlFile
    from mrfix1033.melodybells.i18n.I18N import I18N
    from mrfix1033.melodybells.utils import QtUtils, CommonUtils, ProgramUtils, Constants
    from mrfix1033.melodybells.logging.Logger import Logger
    from mrfix1033.melodybells.utils.ErrorUtils import ErrorUtils
    from mrfix1033.melodybells.windows.MainWindow import MainWindow
    app = QApplication(sys.argv)
    melody_bells = MelodyBells()
    melody_bells.main_window.show()
    app.exec()

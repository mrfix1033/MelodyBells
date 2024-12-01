import logging


class Logger:
    def __init__(self, filename):
        self.logger = logging.Logger(filename)

    def info(self, description):
        self.logger.info(description)

    def warning(self, description):
        self.logger.warning(description)

    def error(self, description):
        self.logger.error(description)

import logging
import sys
import traceback
from typing import Callable, Any

from mrfix1033.melodybells.i18n.I18N import I18N
from mrfix1033.melodybells.utils import QtUtils

__actions_aimed_at_reporting_error__ = [
    "Сделайте скрин или сфоткайте экран и отправьте фото"
]


class ErrorUtils:
    def __init__(self, i18n: I18N, logger: logging.Logger):
        self.i18n = i18n
        self.logger = logger
        self.counter = 1

    def register(self):
        __set_exception_handler__(self.exception_handler)

    def exception_handler(self, exctype: Exception, value: str, trace):
        formatted_exception_string = __build_string_exception__(exctype, value, trace, self.counter)
        self.counter += 1

        description_list = ["Произошла непредвиденная ошибка. Сообщите, пожалуйста, разработчику:"]
        for enum in enumerate(__actions_aimed_at_reporting_error__):
            index, action = enum
            description_list.append(__build_action_string__(index, action))
        description = '\n'.join(description_list)

        QtUtils.open_error_window("Ошибка!", description + formatted_exception_string)
        self.logger.error(formatted_exception_string)


def __build_string_exception__(exctype: Exception, value: str, trace, counter: int):
    trace_string = __format_traceback__(trace)
    return f"Exception #{counter}:\n" \
           f"Class: {exctype.__name__}\n" \
           f"description: {value}\n" \
           f"traceback:\n" \
           f"{trace_string}"


def __set_exception_handler__(handler: Callable[[Exception, str, Any], None]):
    sys.excepthook = handler


def __format_traceback__(trace):
    return ''.join(traceback.format_tb(trace))


def __build_action_string__(index, action):
    return f"{index}) {action}"

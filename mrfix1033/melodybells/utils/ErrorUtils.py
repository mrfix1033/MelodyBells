import sys
import traceback
import typing
from typing import Callable, Any

from mrfix1033.melodybells.logging.Logger import Logger
from mrfix1033.melodybells.utils import QtUtils

__actions_aimed_at_reporting_error__ = [
    "Take a screenshot or take a picture of the screen",
    "Send the photo to the developer",
    "E-mail: mrfix1033@mail.ru (in the subject, specify \"MelodyBells error\")",
    "VK/Telegram: @mrfix1033",
    "Discord: mrfix1033"
]


class ErrorUtils:
    def __init__(self):
        self.logger: typing.Any[Logger, None] = None
        self.error_counter = 1

    def set_logger(self, logger: Logger):
        self.logger = logger

    def register(self):
        _set_exception_handler(self._exception_handler)

    def _exception_handler(self, exctype: Exception, value: str, trace):
        formatted_exception_string = _build_string_exception(exctype, value, trace, self.error_counter)
        self.error_counter += 1

        description_list = ["An unexpected error has occurred. Please inform the developer:"]
        for enum in enumerate(__actions_aimed_at_reporting_error__):
            index, action = enum
            description_list.append(_build_action_string(index, action))
        description = '\n'.join(description_list)

        print(formatted_exception_string)
        QtUtils.open_error_window("Error!", description + formatted_exception_string)
        if self.logger is not None:
            self.logger.error(formatted_exception_string)


def _build_action_string(index, action):
    return f"{index}) {action}"


def _build_string_exception(exctype: Exception, value: str, trace, counter: int):
    trace_string = _format_traceback(trace)
    return f"Exception #{counter}:\n" \
           f"{exctype.__name__}: {value}\n" \
           f"traceback:\n" \
           f"{trace_string}"


def _set_exception_handler(handler: Callable[[Exception, str, Any], None]):
    sys.excepthook = handler


def _format_traceback(trace):
    return ''.join(traceback.format_tb(trace))

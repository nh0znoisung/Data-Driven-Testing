from typing import Optional
from typing import Sequence

class BaseException(Exception):
    """Base webdriver exception."""

    def __init__(
        self, msg: Optional[str] = None, screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None
    ) -> None:
        super().__init__()
        self.msg = msg
        self.screen = screen
        self.stacktrace = stacktrace

    def __str__(self) -> str:
        exception_msg = f"Message: {self.msg}\n"
        if self.screen:
            exception_msg += "Screenshot: available via screen\n"
        if self.stacktrace:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += f"Stacktrace:\n{stacktrace}"
        return exception_msg


class CurrentPasswordNotFillException(BaseException):
    """Thrown when current password form is not filled"""

class NewPasswordNotFillException(BaseException):
    """Thrown when new password form is not filled"""

class AgainPasswordNotFillException(BaseException):
    """Thrown when new password again form is not filled"""

class CurrentPasswordNotCorrectException(BaseException):
    """Thrown when current password form is not correted"""

class InvalidRefillNewPasswordException(BaseException):
    """Thrown when new password form and new password again form do not have the same value"""

class InvalidLengthException(BaseException):
    """Thrown when new password form and new password again is the same but the length of the password is smaller than 8 characters long"""

class InvalidSpecialCharacterException(BaseException):
    """Thrown when new password form and new password again is the same but the length of the password has no special characters such as *,- and #"""
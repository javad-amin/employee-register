from dataclasses import dataclass
from typing import Final


class ResponseStatus:
    FAILURE: Final = "failure"
    SUCCESS: Final = "success"


@dataclass
class DatabaseResponse:
    content: dict | list
    status: str = ResponseStatus.SUCCESS

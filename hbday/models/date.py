from dataclasses import dataclass
from datetime import datetime


@dataclass
class Date:
    month: int
    day: int

    @classmethod
    def now(cls) -> "Date":
        current = datetime.now()
        return cls(month=current.month, day=current.day)

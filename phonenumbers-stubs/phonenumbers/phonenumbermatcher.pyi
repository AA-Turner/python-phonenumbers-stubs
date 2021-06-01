from re import Match
from typing import Iterator, Optional

from .phonenumber import PhoneNumber
from .util import UnicodeMixin

class Leniency:
    POSSIBLE: int = ...
    VALID: int = ...
    STRICT_GROUPING: int = ...
    EXACT_GROUPING: int = ...

class PhoneNumberMatcher:
    text: Optional[str] = ...
    preferred_region: Optional[str] = ...
    leniency: int = ...
    def __init__(self, text: Optional[str], region: Optional[str], leniency: Optional[int] = ..., max_tries: int = ...) -> None: ...
    def has_next(self) -> bool: ...
    def next(self) -> Match[str]: ...
    def __iter__(self) -> Iterator[Match[str]]: ...

class PhoneNumberMatch(UnicodeMixin):
    start: int = ...
    raw_string: str = ...
    end: int = ...
    number: PhoneNumber = ...
    def __init__(self, start: int, raw_string: str, numobj: PhoneNumber) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __unicode__(self) -> str: ...

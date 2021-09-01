from re import Pattern
from typing import Callable, Iterator

from .phonemetadata import NumberFormat
from .phonenumber import PhoneNumber
from .util import UnicodeMixin

def _limit(lower: int, upper: int) -> str: ...

_OPENING_PARENS: str
_CLOSING_PARENS: str
_NON_PARENS: str
_BRACKET_PAIR_LIMIT: str
_MATCHING_BRACKETS: Pattern[str]
_LEAD_LIMIT: str
_PUNCTUATION_LIMIT: str
_DIGIT_BLOCK_LIMIT: int
_BLOCK_LIMIT: str
_PUNCTUATION: str
_DIGIT_SEQUENCE: str
_LEAD_CLASS_CHARS: str
_LEAD_CLASS: str
_LEAD_PATTERN: str
_PATTERN: Pattern[str]
_PUB_PAGES: Pattern[str]
_SLASH_SEPARATED_DATES: Pattern[str]
_TIME_STAMPS: Pattern[str]
_TIME_STAMPS_SUFFIX: Pattern[str]
_INNER_MATCHES: tuple[Pattern[str], ...]

class Leniency:
    POSSIBLE: int = ...
    VALID: int = ...
    STRICT_GROUPING: int = ...
    EXACT_GROUPING: int = ...

def _verify(leniency: int, numobj: PhoneNumber, candidate: str, matcher: PhoneNumberMatcher) -> bool: ...
def _verify_strict_grouping(numobj: PhoneNumber, candidate: str, matcher: PhoneNumberMatcher) -> bool: ...
def _all_number_groups_remain_grouped(numobj: PhoneNumber, normalized_candidate: str, formatted_number_groups: list[str]) -> bool: ...
def _verify_exact_grouping(numobj: PhoneNumber, candidate: str, matcher: PhoneNumberMatcher) -> bool: ...
def _all_number_groups_are_exactly_present(numobj: PhoneNumber, normalized_candidate: str, formatted_number_groups: list[str]) -> bool: ...
def _get_national_number_groups_without_pattern(numobj: PhoneNumber) -> list[str]: ...
def _get_national_number_groups(numobj: PhoneNumber, formatting_pattern: NumberFormat) -> list[str]: ...
def _contains_more_than_one_slash_in_national_number(numobj: PhoneNumber, candidate: str) -> bool: ...
def _contains_only_valid_x_chars(numobj: PhoneNumber, candidate: str) -> bool: ...
def _is_national_prefix_present_if_required(numobj: PhoneNumber) -> bool: ...

class PhoneNumberMatcher:
    _NOT_READY: int
    _READY: int
    _DONE: int
    text: str
    preferred_region: str | None
    leniency: int
    _max_tries: int
    _state: int
    _last_match: PhoneNumberMatch | None
    _search_index: int
    def __init__(self, text: str | None, region: str | None, leniency: int = ..., max_tries: int = ...) -> None: ...
    def _find(self, index: int) -> PhoneNumberMatch | None: ...
    def _trim_after_first_match(self, pattern: Pattern[str], candidate: str) -> str: ...
    @classmethod
    def _is_latin_letter(cls, letter: str) -> bool: ...
    @classmethod
    def _is_invalid_punctuation_symbol(cls, character: str) -> bool: ...
    def _extract_match(self, candidate: str, offset: int) -> PhoneNumberMatch | None: ...
    def _extract_inner_match(self, candidate: str, offset: int) -> PhoneNumberMatch | None: ...
    def _parse_and_verify(self, candidate: str, offset: int) -> PhoneNumberMatch | None: ...
    def _check_number_grouping_is_valid(self, numobj: PhoneNumber, candidate: str, checker: Callable[[PhoneNumber, str, list[str]], bool]) -> bool: ...
    def has_next(self) -> bool: ...
    def next(self) -> PhoneNumberMatch: ...
    def __iter__(self) -> Iterator[PhoneNumberMatch]: ...

class PhoneNumberMatch(UnicodeMixin):
    start: int = ...
    raw_string: str = ...
    end: int = ...
    number: PhoneNumber = ...
    def __init__(self, start: int, raw_string: str, numobj: PhoneNumber) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __unicode__(self) -> str: ...

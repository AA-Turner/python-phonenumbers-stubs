from re import Pattern
from typing import Optional, Union

from .phonemetadata import NumberFormat
from .phonenumber import PhoneNumber
from .util import UnicodeMixin

COUNTRY_CODE_TO_REGION_CODE: dict[int, tuple[str, ...]]
UNKNOWN_REGION: str
NON_DIGITS_PATTERN: Pattern[str]

class PhoneNumberFormat:
    E164: int = ...
    INTERNATIONAL: int = ...
    NATIONAL: int = ...
    RFC3966: int = ...

class PhoneNumberType:
    FIXED_LINE: int = ...
    MOBILE: int = ...
    FIXED_LINE_OR_MOBILE: int = ...
    TOLL_FREE: int = ...
    PREMIUM_RATE: int = ...
    SHARED_COST: int = ...
    VOIP: int = ...
    PERSONAL_NUMBER: int = ...
    PAGER: int = ...
    UAN: int = ...
    VOICEMAIL: int = ...
    UNKNOWN: int = ...
    @classmethod
    def values(cls) -> tuple[int, ...]: ...

class MatchType:
    NOT_A_NUMBER: int = ...
    NO_MATCH: int = ...
    SHORT_NSN_MATCH: int = ...
    NSN_MATCH: int = ...
    EXACT_MATCH: int = ...

class ValidationResult:
    IS_POSSIBLE: int = ...
    IS_POSSIBLE_LOCAL_ONLY: int = ...
    INVALID_COUNTRY_CODE: int = ...
    TOO_SHORT: int = ...
    INVALID_LENGTH: int = ...
    TOO_LONG: int = ...

SUPPORTED_REGIONS: set[str]
COUNTRY_CODES_FOR_NON_GEO_REGIONS: set[str]

def normalize_digits_only(number: str, keep_non_digits: bool = ...) -> str: ...
def normalize_diallable_chars_only(number: str) -> str: ...
def convert_alpha_characters_in_number(number: str) -> str: ...
def length_of_geographical_area_code(numobj: PhoneNumber) -> int: ...
def length_of_national_destination_code(numobj: PhoneNumber) -> int: ...
def country_mobile_token(country_code: int) -> str: ...
def supported_calling_codes() -> set[int]: ...
def supported_types_for_region(region_code: Optional[str]) -> set[int]: ...
def supported_types_for_non_geo_entity(country_code: int) -> set[int]: ...
def is_number_geographical(numobj: PhoneNumber) -> bool: ...
def is_number_type_geographical(num_type: int, country_code: int) -> bool: ...
def format_number(numobj: PhoneNumber, num_format: int) -> str: ...
def format_by_pattern(numobj: PhoneNumber, number_format: int, user_defined_formats: list[NumberFormat]) -> str: ...
def format_national_number_with_carrier_code(numobj: PhoneNumber, carrier_code: str) -> str: ...
def format_national_number_with_preferred_carrier_code(numobj: PhoneNumber, fallback_carrier_code: str) -> str: ...
def format_number_for_mobile_dialing(numobj: PhoneNumber, region_calling_from: str, with_formatting: bool) -> str: ...
def format_out_of_country_calling_number(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def format_in_original_format(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def format_out_of_country_keeping_alpha_chars(numobj: PhoneNumber, region_calling_from: str) -> str: ...
def national_significant_number(numobj: PhoneNumber) -> str: ...
def example_number(region_code: str) -> Optional[PhoneNumber]: ...
def invalid_example_number(region_code: str) -> Optional[PhoneNumber]: ...
def example_number_for_type(region_code: str, num_type: int) -> Optional[PhoneNumber]: ...
def example_number_for_non_geo_entity(country_calling_code: int) -> Optional[PhoneNumber]: ...
def number_type(numobj: PhoneNumber) -> int: ...
def is_valid_number(numobj: PhoneNumber) -> bool: ...
def is_valid_number_for_region(numobj: PhoneNumber, region_code: str) -> bool: ...
def region_code_for_number(numobj: PhoneNumber) -> str: ...
def region_code_for_country_code(country_code: int) -> str: ...
def region_codes_for_country_code(country_code: int) -> tuple[str, ...]: ...
def country_code_for_region(region_code: str) -> int: ...
def country_code_for_valid_region(region_code: str) -> int: ...
def ndd_prefix_for_region(region_code: str, strip_non_digits: bool) -> str: ...
def is_nanpa_country(region_code: str) -> bool: ...
def is_alpha_number(number: str) -> bool: ...
def is_possible_number(numobj: PhoneNumber) -> bool: ...
def is_possible_number_for_type(numobj: PhoneNumber, numtype: int) -> bool: ...
def is_possible_number_with_reason(numobj: PhoneNumber) -> bool: ...
def is_possible_number_for_type_with_reason(numobj: PhoneNumber, numtype: int) -> bool: ...
def is_possible_number_string(number: str, region_dialing_from: str) -> bool: ...
def truncate_too_long_number(numobj: PhoneNumber) -> bool: ...
def parse(
    number: Optional[str],
    region: Optional[str] = ...,
    keep_raw_input: bool = ...,
    numobj: Optional[PhoneNumber] = ...,
    _check_region: bool = ...,
) -> PhoneNumber: ...
def is_number_match(num1: Union[PhoneNumber, str], num2: Union[PhoneNumber, str]) -> bool: ...
def can_be_internationally_dialled(numobj: PhoneNumber) -> bool: ...
def is_mobile_number_portable_region(region_code: str) -> bool: ...

class NumberParseException(UnicodeMixin, Exception):
    INVALID_COUNTRY_CODE: int = ...
    NOT_A_NUMBER: int = ...
    TOO_SHORT_AFTER_IDD: int = ...
    TOO_SHORT_NSN: int = ...
    TOO_LONG: int = ...
    error_type: int = ...
    def __init__(self, error_type: int, msg: str) -> None: ...
    def __reduce__(self) -> tuple[type[NumberParseException], tuple[int, str]]: ...
    def __unicode__(self) -> str: ...

from .phonenumber import PhoneNumber

SUPPORTED_SHORT_REGIONS: list[str]

class ShortNumberCost:
    TOLL_FREE: int = ...
    STANDARD_RATE: int = ...
    PREMIUM_RATE: int = ...
    UNKNOWN_COST: int = ...

def is_possible_short_number_for_region(short_numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_possible_short_number(numobj: PhoneNumber) -> bool: ...
def is_valid_short_number_for_region(short_numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_valid_short_number(numobj: PhoneNumber) -> bool: ...
def expected_cost_for_region(short_numobj: PhoneNumber, region_dialing_from: str) -> int: ...
def expected_cost(numobj: PhoneNumber) -> int: ...
def connects_to_emergency_number(number: str, region_code: str) -> bool: ...
def is_emergency_number(number: str, region_code: str) -> bool: ...
def is_carrier_specific(numobj: PhoneNumber) -> bool: ...
def is_carrier_specific_for_region(numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
def is_sms_service_for_region(numobj: PhoneNumber, region_dialing_from: str) -> bool: ...
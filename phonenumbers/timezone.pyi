from .phonenumber import PhoneNumber

UNKNOWN_TIMEZONE: str

def time_zones_for_geographical_number(numobj: PhoneNumber) -> tuple[str, ...]: ...
def time_zones_for_number(numobj: PhoneNumber) -> tuple[str, ...]: ...
from enum import IntEnum


class Role(IntEnum):
    MANAGER = 1
    WAITER = 2
    ADMIN = 3


ROLE_MAP = {1: "MANAGER", 2: "WAITER", 3: "CAISHER"}

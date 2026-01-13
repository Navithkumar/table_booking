from enum import IntEnum


class Status(IntEnum):
    AVAILABLE = 1
    OCCUPIED = 2
    BILL_REQUESTED = 3
    CLOSED = 4

import enum

class TransitionsEnum(enum.Enum):
    FINISH_SERVICE = 0
    BREAK = 1
    FIX = 2
    DOORS_CLOSED = 3
    ONE_BROKEN = 4
    ALL_FIXED = 5
    CALL = 6

import enum


class TransitionsEnum(enum.Enum):
    FINISH_SERVICE = 0
    BREAK = 1
    FIX = 2
    DOORS_CLOSED = 3
    ONE_BROKEN = 4
    ALL_FIXED = 5
    # simulation start
    START_SUMILATION = 6
    CALL = 7
    NEW_ARRIVAL = 8

from enum import Enum, auto

class NailInteractionType(Enum):
    NO_INTERACT = auto()
    BREAKABLE = auto()
    KNOCKBACK = auto()
    DAMAGE = auto()
    DAMAGE_NO_KNOCKBACK = auto()
    SOFT_KNOCKBACK = auto()
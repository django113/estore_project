from enum import Enum


class cartStatusEnumTypes(Enum):
    CART = "CART"
    WISHLIST = "WISHLIST"

    @classmethod
    def choices(cls):
        return [(key.value,key.name) for key in cls]

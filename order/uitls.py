from enum import Enum


class orderStatusEnumTypes(Enum):
    CANCEL = "CANCEL"
    PENDING = "PENDING"
    OUT_OF_DELIVERY = "OUT_OF_DELIVERY"
    DELIVERED = "DELIVERED"

    @classmethod
    def choices(cls):
        return [(key.value,key.name) for key in cls]

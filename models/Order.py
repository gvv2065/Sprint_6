from enum import Enum


class Order:
    class Color(Enum):
        black = 'чёрный жемчуг'
        grey = 'серая безысходность'
    
    class Duration(Enum):
        TWO_DAYS = 'двое суток'
        FOUR_DAYS = 'четверо суток'

    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._address = ""
        self._subway_station = ""
        self._phone = ""
        self._color = None
        self._comment = ""
        self._rent_duration = None

    def set_first_name(self, value: str):
        self._first_name = value
        return self

    def set_last_name(self, value: str):
        self._last_name = value
        return self

    def set_address(self, value: str):
        self._address = value
        return self

    def set_subway_station(self, value: str):
        self._subway_station = value
        return self

    def set_phone(self, value: str):
        self._phone = value
        return self

    def set_color(self, value: 'Order.Color'):
        self._color = value
        return self
    
    def set_rent_duration(self, value: 'Order.Duration'):
        self._rent_duration = value
        return self

    def set_comment(self, value: str):
        self._comment = value
        return self

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_address(self) -> str:
        return self._address

    def get_subway_station(self) -> str:
        return self._subway_station

    def get_phone(self) -> str:
        return self._phone

    def get_color(self) -> 'Order.Color':
        return self._color
    
    def get_rent_duration(self) -> 'Order.Duration':
        return self._rent_duration

    def get_comment(self) -> str:
        return self._comment
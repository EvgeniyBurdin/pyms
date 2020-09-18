from dataclasses import dataclass, field

from data_classes.base import ApiDC


@dataclass
class PeapleData(ApiDC):
    """ Параметры для создания записи таблицы peaple.
    """
    name: str
    extra: dict = field(default_factory=dict)

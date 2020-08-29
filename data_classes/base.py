""" Модуль родителя всех API-датаклассов.
"""
from dataclasses import dataclass

from validated_dc import ValidatedDC


@dataclass
class ApiDC(ValidatedDC):
    pass

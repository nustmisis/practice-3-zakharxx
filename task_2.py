# -*- coding: utf-8 -*-
"""
Напишите функцию которая на вход получает строку с госномером автомобиля и
выводит к какому типу относится данный госномер, или возвращает Fail! если это
не госномер.

Типы гос.номеров:

Тип |    Пример
----+----------
 1А | с227на 69
 1Б |  ао365 78
  2 | ан7331 47
  3 | 3733мм 55

Для корректной работы автоматических тестов не переименовывайте функцию
get_plate_type!
"""


import re

def get_plate_type(license_plate):
    patterns = [
        (r'^[АВЕКМНОРСТУХAEEKMHOPCTYX]{1}\d{3}[АВЕКМНОРСТУХAEEKMHOPCTYX]{2}\s\d{2}$', '1А'),
        (r'^[АВЕКМНОРСТУХAEEKMHOPCTYX]{2}\d{3}[АВЕКМНОРСТУХAEEKMHOPCTYX]{1}\s\d{2}$', '1А'),
        (r'^[АВЕКМНОРСТУХAEEKMHOPCTYX]{2}\d{3}\s\d{2}$', '1Б'),
        (r'^[АВЕКМНОРСТУХAEEKMHOPCTYX]{2}\d{4}\s\d{2}$', '2'),
        (r'^\d{4}[АВЕКМНОРСТУХAEEKMHOPCTYX]{2}\s\d{2}$', '3')
    ]

    license_plate = license_plate.upper()

    for pattern, plate_type in patterns:
        if re.match(pattern, license_plate):
            return plate_type

    return "Fail!"
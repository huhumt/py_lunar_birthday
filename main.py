#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from converter import Lunar
from ics import generate_ics_file
from datetime import timedelta

birthday_list = [
    {
    "name": "野比大雄生日",
    "date": dict(year=2008, month=1, day=3),
    },
    {
    "name": "源靜香生日",
    "date": dict(year=2009, month=3, day=9),
    },
    {
    "name": "骨川小夫生日",
    "date": dict(year=2008, month=2, day=17),
    },
    {
    "name": "剛田胖虎生日",
    "date": dict(year=2008, month=1, day=1),
    }
]
ics_info_list = []

for person in birthday_list:
    birthday_lunar = Lunar.from_date(type('Auto', (), person["date"]))

    for year in range(birthday_lunar.year, min(birthday_lunar.year + 100, 2100)):
        year_birthday = Lunar(year, birthday_lunar.month, birthday_lunar.day).to_date()
        ics_info_list.append(
            {
                "name": person.get("name"),
                "date_start": year_birthday.strftime("%Y%m%d"),
                "date_end": (year_birthday + timedelta(days=1)).strftime("%Y%m%d"),
                "description": f"祝{person.get('name')}快樂，永遠愛你們哦！"
            }
        )
generate_ics_file(ics_info_list)

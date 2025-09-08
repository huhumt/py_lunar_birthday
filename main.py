#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from converter import Lunar
from ics import IcsEvent, generate_ics_file

from collections import OrderedDict
from base64 import b16encode
from datetime import date, timedelta

birthday_dict = {
    "野比大雄生日": {
        # this is from solar calendar date
        "date": date(year=2008, month=1, day=3),
    },
    "源靜香生日": {
        "date": date(year=2009, month=3, day=9),
    },
    "骨川小夫生日": {
        "date": date(year=2008, month=2, day=17),
    },
    "剛田胖虎生日": {
        "date": date(year=2008, month=1, day=1),
    }
}
ics_info_dict = OrderedDict()

for k, v in birthday_dict.items():
    birthday_lunar = Lunar.from_date(v["date"])

    for year in range(birthday_lunar.year, min(birthday_lunar.year + 100, 2100)):
        year_birthday = Lunar(year, birthday_lunar.month, birthday_lunar.day).to_date()
        year_birthday_date = year_birthday.strftime("%Y%m%d")
        uid = b16encode(f'{k}{year_birthday_date}'.encode()).decode()
        ics_info_dict[uid] = IcsEvent(
            k,
            year_birthday_date,
            (year_birthday + timedelta(days=1)).strftime("%Y%m%d"),
            f"祝{k}快樂，永遠愛你們哦！"
        )
generate_ics_file(ics_info_dict)

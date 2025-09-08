#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional

calendar_template: str = """BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
NAME:lunar_calendar_event
X-WR-CALNAME:lunar_calendar_event
X-WR-TIMEZONE:Asia/Taipei
{event}
END:VCALENDAR"""

event_template: str = """BEGIN:VEVENT
UID:{uid}@lunar_calendar.py
SEQUENCE:0
DTSTAMP:{generate_timestamp}
DTSTART;VALUE=DATE:{date_start}
DTEND;VALUE=DATE:{date_end}
X-MICROSOFT-CDO-ALLDAYEVENT:TRUE
X-MICROSOFT-MSNCALENDAR-ALLDAYEVENT:TRUE
SUMMARY:{summary}
STATUS:CONFIRMED
DESCRIPTION:{description}
END:VEVENT"""

@dataclass
class IcsEvent:
    event: str       # event name
    start_date: str  # event start date
    end_date: str    # event end date
    description: Optional[str] = None


def generate_ics_file(event_dict: OrderedDict[str, IcsEvent], filename: str = "lunar_calendar.ics"):
    """generate ics file with given information"""
    timestamp = datetime.now().strftime('%Y%m%dT%H%M%SZ')
    with open(filename, "w", encoding="utf-8", newline='\r\n') as f:
        f.write(calendar_template.format(event="\n".join([
            event_template.format(
                uid = k,
                generate_timestamp=timestamp,
                date_start=v.start_date,
                date_end=v.end_date,
                summary=v.event,
                description=v.description or v.event
            ) for k, v in event_dict.items()])
        ))


if __name__ == "__main__":
    """for test purpose only"""
    event_dict = OrderedDict({
        "1234": IcsEvent(
            "test001",
            "20250102",
            "20250103",
            "good test"
        ),
        "5678": IcsEvent(
            "test002",
            "20251112",
            "20251113"
        )
    })
    generate_ics_file(event_dict)

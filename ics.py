#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from uuid import uuid4

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
UID:{uuid}@lunar_calendar.py
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


def generate_ics_file(event_list: list, filename: str = "lunar_calendar.ics"):
    """generate ics file with given information"""
    timestamp = datetime.now().strftime('%Y%m%dT%H%M%SZ')
    with open(filename, "w", encoding="utf-8", newline='\r\n') as f:
        f.write(calendar_template.format(event="\n".join([
            event_template.format(
                uuid = uuid4().hex,
                generate_timestamp=timestamp,
                date_start=event.get("date_start"),
                date_end=event.get("date_end"),
                summary=event.get("name"),
                description=event.get("description")
            ) for event in event_list])
        ))


if __name__ == "__main__":
    """for test purpose only"""
    event_list = [
        {
            "name": "test001",
            "date_start": "20250102",
            "date_end": "20250103",
            "description": "good test"
        },
        {
            "name": "test002",
            "date_start": "20251112",
            "date_end": "20251113",
            "description": "good test"
        }
    ]
    generate_ics_file(event_list)

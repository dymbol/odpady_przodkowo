from icc import Calendar, Event  # Organized imports by standard library first and third-party libraries after
from datetime import datetime, timedelta, timezone
import data.parsed_data as parsed_data


gmt_plus_2 = timezone(timedelta(hours=2))
    
ics_types=["colored","plain"]
event_types=["BIO","POPIÓŁ","ZMIESZANE","PAPIER","SZKŁO","PLASTIK","TERMIN PŁATNOŚCI"]
event_emot = {
    "BIO": "🟫",
    "POPIÓŁ": "⬜",
    "ZMIESZANE": "⬛",
    "PAPIER": "🟦",
    "SZKŁO": "🟩",
    "PLASTIK": "🟨",
    "TERMIN PŁATNOŚCI": "💵",
}

def convert_date(date: str, year: str) -> datetime:
    # format in: DD.MM  
    full_date_string = f"{date}.{year}"
    date_obj = datetime.strptime(full_date_string, "%d.%m.%Y").replace(tzinfo=gmt_plus_2)
    return date_obj

for element in parsed_data.data_places:
    for ics_type in ics_types:
        c = Calendar()
        c.creator='https://github.com/dymbol/odpady_przodkowo'
        c.name=f'Harmonogram wywozu odpaów dla miejscowści: {element["miejscowości"]}'
        c.organizer="Gmina Przodkowo"

        with open(f'data/{element["rok"]}_{element["miejscowości"]}_{ics_type}.ics',"w",newline="") as my_calendar:
            for event_type in event_types:

                waste_name = ""
                if ics_type == "colored":
                    waste_name = f"{event_emot[event_type]} {event_type}"
                elif ics_type == "plain":
                    waste_name = event_type

                for event_date in element[event_type]:
                    e = Event()
                    e.name = waste_name
                    e.summary = waste_name
                    e.description = f" wywóz odpadów: {waste_name}"
                    e.begin = convert_date(event_date,element["rok"])
                    e.begin = convert_date(event_date,element["rok"]) + timedelta(hours=7)
                    e.end = convert_date(event_date,element["rok"]) + timedelta(hours=17)
                    e.all_day: True
                    c.events.add(e)        
            my_calendar.write(c.serialize())

from ics import Calendar, Event
from datetime import datetime
import data.parsed_data as parsed_data

event_types=["BIO","POPIÓŁ","ZMIESZANE","PAPIER","SZKŁO","PLASTIK","TERMIN PŁATNOŚCI"]

def convert_date(date, year):
    # format in: DD.MM
    full_date_string = f"{date}.{year}"
    date_obj = datetime.strptime(full_date_string, "%d.%m.%Y")
    return date_obj


for element in parsed_data.data_places:
    c = Calendar()
    c.name=f'Harmonogram wywozu odpaów dla miejscowści: {element["miejscowości"]}'
    c.organizer="Gmina Przodkowo"

    with open(f'data/{element["rok"]}_{element["miejscowości"]}.ics',"w",newline="") as my_calendar:
        for event_type in event_types:
            for event_date in element[event_type]:
                e = Event()
                e.summary = event_type
                e.description = event_type
                e.begin = convert_date(event_date,element["rok"])
                e.all_day: True
                c.events.add(e)        
        my_calendar.write(c.serialize())
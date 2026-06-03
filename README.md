# Kalendarz wywozu odpadów dla Gminy Przodkowo
Gmina Przodkowo udostępnia kalendarze wywozu odpadów w formie papierowej oraz pliów pdf. W celu dodania dni wywozu do kalendarzy elektronicznych (np.: Google Calendar) i systemów Automatyzacji, należy takie dane wprowadzić.
To repozytorium zawiera informacje:
- jak zautomatyzowć proces konwersji danych z pliku pdf do formatu [ICS](https://pl.wikipedia.org/wiki/ICalendar)
- udostępnia kalendarze w formatacie ICS

## Żródło danych
Źródłem danych jest oficjalna strona internetowa Gminy Przodkowo: (https://www.przodkowo.pl/index.php?s=wpisy&id=56)

## Użycie skryptu do generowanie kalendarzy ICS
- stwórz ręcznie lub przy pomocy LLMa plik `data/parsed_data.py` zgodnie z plikiem `parsed_data.py_EXAMPLE`
```
poetry install
poetry run python generate_calendars.py
```
- pliki ICS trafią do katalogu `data`

### Konwersja harmonogramów z pdf do png (Linux Manjaro)
```cd data/source/2026/pdf
for f in *.pdf; do convert -density 150 "$f" ../img/"${f%.pdf}.png"; done
```
### Załącz pliki kalendarza w formacie graficznym png. LLMy nie działają poprawnie z plikami PDF

### Prompt
Analiza uzycia róznych narzędzi AI:
- Google Gemini -> błędna analiza
- Grok -> Błędna analiza
- ChatGPT -> poprawna analiza (z drobnymi błędami)

```
Pliki to kalendarz wywozu odpadów na 2026 rok.

Każdy kwadrat z szarą obramówką reprezentuje miesiąc.
Każda liczba w tym kwadracie oznacza dzień miesiąca.

Dzień wywozu może być oznaczony:
- kolorem tła liczby,
- kolorem obramowania liczby,
- lub jednocześnie kolorem tła i obramowania.

Kolor obramowania ma takie samo znaczenie jak kolor tła.

Następnie zweryfikuj, że liczba znalezionych terminów dla każdej kategorii
(BIO, POPIÓŁ, ZMIESZANE, PAPIER, SZKŁO, PLASTIK, TERMIN PŁATNOŚCI)
odpowiada wszystkim oznaczeniom widocznym w kalendarzu.

Nie pomijaj pojedynczych oznaczeń występujących tylko raz w miesiącu.

Mapowanie kolorów:
- BIO — brązowy
- POPIÓŁ — szary
- ZMIESZANE — czarny
- PAPIER — niebieski
- SZKŁO — zielony
- PLASTIK — żółty
- TERMIN PŁATNOŚCI — czerwona ramka

Jeżeli dzień posiada zarówno kolorowe tło jak i kolorową ramkę:
- uwzględnij wszystkie odpowiadające im kategorie,
- jeden dzień może należeć do wielu kategorii.

Na podstawie tego stwórz obiekt słownika w Pythonie.

rok = 2026
miejscowości:  maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko
organizator: Gmina Przodkowo
miesjcowości:
- pobierz z nazwy pliku,
- usuń rozszerzenie,
- usuń początkowy znacznik daty (np. 20251216074741_),
- usuń postfix "_nowe",
- pozostałą część pozostaw bez zmian.


Przed wygenerowaniem wyniku sprawdź wszystkie dni z kolorowym tłem ORAZ wszystkie dni z kolorowym obramowaniem.
Nie pomijaj dni oznaczonych wyłącznie obramowaniem.

Przykład:

[
    {
    "rok": 2026,
    "miejscowości": "maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko",
    "organizator": "Gmina Przodkowo",
    "BIO":["20.01",],
    "POPIÓŁ": [],
    "ZMIESZANE": [],
    "PAPIER": [],
    "SZKŁO": [],
    "PLASTIK": [],
    "TERMIN PŁATNOŚCI": ["15.03","15.05","15.09","15.11"],
    },
]
```
## Integracja z Home Assistant
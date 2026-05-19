# Kalendarz wywozu odpadów dla Gminy Przodkowo
Gmina Przodkowo udostępnia kalendarze wywozu odpadów w formie papierowej oraz pliów pdf. W celu dodania dni wywozu do kalendarzy elektronicznych (np.: Google Calendar) i systemów Automatyzacji, należy takie dane wprowadzić.
To repozytorium zawiera informacje:
- jak zautomatyzowć proces konwersji danych z pliku pdf do formatu [ICS](https://pl.wikipedia.org/wiki/ICalendar)
- udostępnia kalendarze w formatacie ICS

## Żródło danych
Źródłem danych jest oficjalna strona internetowa Gminy Przodkowo: (https://www.przodkowo.pl/index.php?s=wpisy&id=56)

## Tabela konwersji
|plik źródłowy|ICS|
| ------------- |:-------------------:|
|[bagniewo_brzeziny_bursztynik_gliniewo_kawle_dolne_kawle_gorne_przodkowo](data/20241212085821_bagniewo_brzeziny_bursztynik_gliniewo_kawle_dolne_kawle_gorne_przodkowo.pdf)||
|[barwik_bielawy_czarna_huta_hejtus_pomieczyno_rab_stanislawy_szarlata_wilanowo](data/20241212085845_barwik_bielawy_czarna_huta_hejtus_pomieczyno_rab_stanislawy_szarlata_wilanowo.pdf)||
|[czeczewo_hopy_klosowo_klosowko_trzy_rzeki_zaleskie_piaski_zaleze](data/20241212085902_czeczewo_hopy_klosowo_klosowko_trzy_rzeki_zaleskie_piaski_zaleze.pdf)||
|[kczewo_kobysewo_kosowo_mlynek_osowa_gora_smoldzino](data/20241212085918_kczewo_kobysewo_kosowo_mlynek_osowa_gora_smoldzino.pdf)|||
|[maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko](data/20241212085946_maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko.pdf)|[text](data/2025_maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko_plain.ics), [kolor](data/2025_maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko_colored.ics)|


## Claude code support.
### Konwwersja harmonogramów z pdf do png(Linux Manjaro)
```cd data/source/2026/pdf
for f in *.pdf; do convert -density 150 "$f" ../img/"${f%.pdf}.png"; done
```
### Załącz pliki kalendarza w formacie graficznym png. Claude nie działa poprawnei z plikami PDF

### Prompt
sPliki to kalendarz na 2026 rok.
Każdy kwadrat z szarą obramówką na górze reprezentuje miesiąc.
Każda liczba w tym kwadracie to dzień miesąca.
Kazda liczba z tłem niebiałym symbolizuje dzień wywozu specyficznych odpadów:
- BIO - brązowy
- POPIÓŁ - szary
- ZMIESZANE - czarny
- PAPIER - niebieski
- SZKŁO - zielony
- PLASTIK - żółty
- TERMIN PŁATNOŚCI - czerwona ramka

Na podstawie tego stwórz obiekt słownika w Pythonie.

rok = 2026
miejscowości = maslowo_nowe_tokary_otalzyno_tokarskie_pnie_tokary_warzenko
organizator = Gmina Przodkowo
miesjcowości = nazwa pliku bez rozszerzenia, początkowych liczb i postfixu _nowe
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
## Integracja z Home Assistant
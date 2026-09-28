events = {
    "Museumsnacht - Dortmund Kunstverein": "19.09.2026",
    "DEW21 Museumsnacht - Dortmunder U": "19.09.2026",
    "Mindful Listening - Konzerthaus Dortmund": "19.09.2026",
    "Die DEW21 Museumsnacht tanzt": "19.09.2026"
}

museum_night_date = "19.09.2026"

print("Events running during the Night of Museums:")

for event, date in events.items():
    if date == museum_night_date:
        print(event)
        
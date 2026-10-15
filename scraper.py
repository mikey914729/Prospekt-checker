import json
# Die neuen Angebote, die der Roboter geholt hat

neue_angebote = [
{"name": "Paulaner Spezi (Kasten 20x0,5l)", "laden": "Lidl", "preis": "7.99 €"},
{"name": "Frische Äpfel Elstar (1kg)", "laden": "Aldi", "preis": "1.11 €"},
{"name": "Paulaner Spezi (0,5l Flasche)", "laden": "Penny", "preis": "0.59 €"},
{"name": "Bio-Äpfel Gala (500g)", "laden": "Penny", "preis": "1.69 €"},
{"name": "Coca-Cola 4er Pack (4x1,25l)", "laden": "Aldi", "preis": "3.29 €"}
]
# Wir schreiben die Daten direkt und sicher in die daten.json

with open("daten.json", "w", encoding="utf-8") as f:
json.dump(neue_angebote, f, ensure_ascii=False, indent=4)
print("Preise erfolgreich in daten.json aktualisiert!")

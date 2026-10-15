import json
import os
# 1. Das Skript tut so, als ob es die neuesten Angebote aus dem Internet geladen hat

neue_angebote = [
{"name": "Paulaner Spezi (Kasten 20x0,5l)", "laden": "Lidl", "preis": "8.99 €"},
{"name": "Frische Äpfel Elstar (1kg)", "laden": "Aldi", "preis": "1.29 €"},
{"name": "Paulaner Spezi (0,5l Flasche)", "laden": "Penny", "preis": "0.69 €"},
{"name": "Bio-Äpfel Gala (500g)", "laden": "Penny", "preis": "1.79 €"},
{"name": "Coca-Cola 4er Pack (4x1,25l)", "laden": "Aldi", "preis": "3.49 €"}
]
# 2. Wir lesen die vorhandene index.html ein

with open("index.html", "r", encoding="utf-8") as f:
html_inhalt = f.read()
# 3. Wir suchen die Stelle, wo die Angebote im JavaScript stehen

start_tag = "// Datenbank (Option A - hier kannst du später erweitern!)"
end_tag = "];"
start_pos = html_content = html_inhalt.find(start_tag)
if start_pos != -1:
# Wir bereiten die neuen Daten im passenden JavaScript-Format vor
js_daten = start_tag + "
const angebote = " + json.dumps(neue_angebote, ensure_ascii=False, indent=12)
# Wir suchen das Ende des alten Blocks
rest_text = html_inhalt[start_pos:]
end_pos_relative = rest_text.find(end_tag)
if end_pos_relative != -1:
end_pos_absolute = start_pos + end_pos_relative + len(end_tag)
# Wir setzen die HTML-Datei mit den BRANDNEUEN Preisen neu zusammen
neues_html = html_inhalt[:start_pos] + js_daten + html_inhalt[end_pos_absolute:]

# 4. Wir speichern die aktualisierte index.html ab

with open("index.html", "w", encoding="utf-8") as f:
f.write(neues_html)
print("Angebote wurden erfolgreich aktualisiert!")

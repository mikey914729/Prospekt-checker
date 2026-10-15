import json
# 1. Die neuen Test-Angebote mit leicht veränderten Preisen

neue_angebote = [
{"name": "Paulaner Spezi (Kasten 20x0,5l)", "laden": "Lidl", "preis": "8.99 €"},
{"name": "Frische Äpfel Elstar (1kg)", "laden": "Aldi", "preis": "1.29 €"},
{"name": "Paulaner Spezi (0,5l Flasche)", "laden": "Penny", "preis": "0.69 €"},
{"name": "Bio-Äpfel Gala (500g)", "laden": "Penny", "preis": "1.79 €"},
{"name": "Coca-Cola 4er Pack (4x1,25l)", "laden": "Aldi", "preis": "3.49 €"}
]
# 2. Bestehendes HTML einlesen

with open("index.html", "r", encoding="utf-8") as f:
html_inhalt = f.read()
# 3. Den Bereich im JavaScript suchen und ersetzen

start_tag = "// Datenbank (Option A - hier kannst du später erweitern!)"
end_tag = "];"
start_pos = html_inhalt.find(start_tag)
if start_pos != -1:
js_daten = start_tag + "
const angebote = " + json.dumps(neue_angebote, ensure_ascii=False, indent=12)
rest_text = html_inhalt[start_pos:]
end_pos_relative = rest_text.find(end_tag)
if end_pos_relative != -1:
end_pos_absolute = start_pos + end_pos_relative + len(end_tag)
neues_html = html_inhalt[:start_pos] + js_daten + html_inhalt[end_pos_absolute:]

# 4. Datei überschreiben

with open("index.html", "w", encoding="utf-8") as f:
f.write(neues_html)
print("Angebote wurden erfolgreich aktualisiert!")
else:
print("Fehler: Start-Tag in index.html nicht gefunden.")

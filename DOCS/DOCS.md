# General Documentation by Housten

---

## Markdown-Grundlagen

### Überschriften
- `#` = Große Überschrift
- `##` = Mittlere Überschrift
- `###` = Kleine Überschrift

### Text
- `**fett**` = **fett**
- `*kursiv*` = *kursiv*

### Aufzählungen
- `-` = Aufzählungspunkt
- `1.` = Nummerierte Liste

### Code
- `` `befehl` `` = einzelner Befehl im Text
- ` ``` ` = ganzer Codeblock

### Trennlinie
- `---` = horizontale Linie

---

## Projekt Setup

### Projektstruktur
So sieht ein sauberes Flask-Projekt aus:

```
data-analytics-engine/
├── static/          → CSS, JavaScript, Bilder
├── templates/       → HTML-Dateien
├── .gitignore
├── .venv/
├── app.py           → Herzstück, Flask-App
├── DOCS.md
└── requirements.txt
```

### Ordner und Dateien erstellen
```
mkdir templates                          → templates Ordner erstellen
mkdir static                             → static Ordner erstellen
echo. > app.py                           → leere Datei erstellen
```

### .venv
Die virtuelle, isolierte Umgebung `.venv` ist nur für dieses Projekt. Pakete die ich dort installiere beeinflussen keine anderen Projekte auf dem PC.

### requirements.txt
Eine Liste aller Pakete damit andere oder ich selbst das Projekt neu aufsetzen können und wissen was gebraucht wird.

### pip freeze
Schaut was alles an Paketen installiert wurde die für das Projekt gebraucht werden und schreibt sie in eine Datei (z.B. `requirements.txt`).

### Befehle
- `python -m venv .venv` = venv erstellen
- `.venv\Scripts\activate` = venv aktivieren
- `python -m pip install flask` = Flask installieren
- `python -m pip freeze > requirements.txt` = requirements erstellen

---

## app.py - Flask Grundstruktur

Das Herzstück der Anwendung. Hier läuft alles zusammen.

```python
from flask import Flask, render_template  # Flask und HTML-Rendering importieren

app = Flask(__name__)                     # Flask-Instanz - immer so, nie anders

@app.route("/")                           # Route für die Startseite
def startseite():
    return render_template("index.html")  # Sucht index.html im templates/ Ordner

if __name__ == "__main__":
    app.run(debug=True)                   # debug=True nur während der Entwicklung!
```

### debug=True
Zeigt bei Fehlern genau wo und was das Problem ist. **Niemals** im fertigen Produkt verwenden - zeigt sensible Infos über den Code!

### App starten
```
python app.py
```
Danach ist die App erreichbar unter: `http://127.0.0.1:5000`

---

## .gitignore

Verhindert dass unnötige oder sensible Dateien ins GitHub Repo hochgeladen werden.

### Wichtige Einträge
- `__pycache__/` = wird von Python automatisch erstellt, braucht niemand im Repo
- `.venv/` = jeder erstellt seine eigene Umgebung mit der `requirements.txt`
- `.env` = sensible Daten wie Passwörter und API Keys - **niemals** ins Repo!
- `instance/` = lokale Flask-Konfigurationen
- `.vscode/` = persönliche Editor-Einstellungen
- `Thumbs.db` = wird von Windows automatisch erstellt, ist Müll

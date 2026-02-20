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

### Route
Eine Route verbindet eine URL mit einer Python-Funktion. Wenn jemand die URL aufruft, wird die Funktion ausgeführt und gibt etwas zurück.
```python
@app.route("/")          # URL die aufgerufen wird
def startseite():        # Funktion die dann ausgeführt wird
    return render_template("index.html")
```

### Route mit Methoden
Standardmäßig akzeptiert eine Route nur GET. Für Formulare braucht man POST:
```python
@app.route("/eintragen", methods=["GET", "POST"])
def eintragen():
    if request.method == "POST":
        # Formular wurde abgeschickt
    return render_template("formular.html")
```

### redirect
Leitet den Browser nach einer Aktion auf eine andere Seite weiter:
```python
return redirect("/")     # leitet zur Startseite weiter
```

### debug=True
Zeigt bei Fehlern genau wo und was das Problem ist. **Niemals** im fertigen Produkt verwenden - zeigt sensible Infos über den Code!

### render_template
`render_template("index.html")` macht drei Dinge:
1. **Sucht** die Datei im `templates/` Ordner
2. **Verarbeitet** sie (kann Python-Variablen einsetzen)
3. **Gibt** das fertige HTML zurück

Erst `return render_template(...)` schickt es wirklich an den Browser!

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

---

## Git & GitHub

### Befehle
```
git init                                  → Git im Projektordner initialisieren
git remote add origin <URL>               → GitHub Repo verbinden
git add .                                 → alle Änderungen stagen
git commit -m "Beschreibung."             → Commit erstellen (immer mit Punkt!)
git push                                  → auf GitHub hochladen
git push -u origin master                 → beim ersten Push
```

### Hinweise
- `git add .` und `git commit` und `git push` = die drei Schritte die man immer braucht
- Commit-Message immer aussagekräftig und mit Punkt am Ende
- Nach jedem sinnvollen Fortschritt committen!

---

## SQLAlchemy & SQLite

### Was ist SQLite?
Eine Datenbank als einzelne `.db` Datei auf dem PC. Kein extra Server nötig - perfekt für kleinere Projekte.

### Was ist SQLAlchemy?
Der Vermittler zwischen Python und der Datenbank. Man schreibt Python-Klassen statt SQL.

### Datenbank konfigurieren
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datenbankname.db'
db = SQLAlchemy(app)
```

### Model (Tabelle) erstellen
Jede Klasse = eine Tabelle. Jede Variable = eine Spalte.
```python
class Uebersicht(db.Model):
    id                      = db.Column(db.Integer, primary_key=True)
    date                    = db.Column(db.DateTime)
    item_name               = db.Column(db.String(100), nullable=False)
    item_quantity           = db.Column(db.Integer, nullable=False)
    purchase_price_per_unit = db.Column(db.Float, nullable=False)
```

### Spalten-Typen
- `db.Integer` = Ganzzahl (keine Klammern!)
- `db.Float` = Dezimalzahl (für Preise)
- `db.String(100)` = Text mit max. 100 Zeichen
- `db.DateTime` = Datum und Uhrzeit

### nullable=False
Das Feld **muss** ausgefüllt sein - darf nicht leer bleiben.

### Datenbank initialisieren
Einmalig ausführen - erstellt die `.db` Datei:
```python
with app.app_context():
    db.create_all()
```

### Eintrag speichern
```python
neuer_eintrag = Uebersicht(
    date      = datetime.now(),
    item_name = request.form["item-name"],
)
db.session.add(neuer_eintrag)
db.session.commit()
```

### Wichtige Imports
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
```

### Paket installieren
```
python -m pip install flask-sqlalchemy
```

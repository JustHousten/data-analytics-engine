# Flask Dokumentation

---

## Was ist Flask?
Ein minimalistisches Python Backend-Framework. Es empfängt Anfragen vom Browser, verarbeitet Daten und gibt Antworten zurück.

---

## Grundstruktur app.py

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def startseite():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Routen

### Einfache Route
```python
@app.route("/")
def startseite():
    return render_template("index.html")
```

### Route mit POST
```python
@app.route("/eintragen", methods=["GET", "POST"])
def eintragen():
    if request.method == "POST":
        wert = request.form["feldname"]
    return render_template("seite.html")
```

---

## Formular-Daten empfangen

```python
# Wert aus einem HTML Input mit name="feldname" holen
wert = request.form["feldname"]
```

**Wichtig:** Der Name in `request.form["..."]` muss exakt dem `name`-Attribut im HTML entsprechen!

---

## render_template
`render_template("index.html")` macht drei Dinge:
1. **Sucht** die Datei im `templates/` Ordner
2. **Verarbeitet** sie (kann Python-Variablen einsetzen)
3. **Gibt** das fertige HTML zurück

Erst `return render_template(...)` schickt es wirklich an den Browser!

```python
return render_template("index.html")
```

---

## redirect
Leitet den Browser nach einer Aktion auf eine andere Seite weiter:
```python
return redirect("/")    # leitet zur Startseite weiter
```

---

## GET vs POST
- **GET** = Daten werden in der URL mitgeschickt (z.B. Suche). Sichtbar für jeden.
- **POST** = Daten werden unsichtbar im Hintergrund geschickt. Für Formulare die Daten speichern.

---

## debug=True
Zeigt bei Fehlern genau wo und was das Problem ist. **Niemals** im fertigen Produkt verwenden!

---

## App starten
```
python app.py
```
Erreichbar unter: `http://127.0.0.1:5000`

# HTML & CSS Dokumentation

---

## HTML Grundstruktur

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seitenname</title>
</head>
<body>
    <!-- Inhalt hier -->
</body>
</html>
```

---

## Formulare

```html
<form action="/route" method="POST">
    <div>
        <label for="feldname">Beschriftung:</label>
        <input type="text" name="feldname" id="feldname">
    </div>
    <button type="submit">Absenden</button>
</form>
```

### Wichtige Attribute
- `action` = wohin die Daten geschickt werden (Flask Route)
- `method` = wie sie geschickt werden (`POST` für Daten speichern, `GET` für Suchen)
- `name` = **entscheidend!** Flask liest die Daten genau über diesen Namen aus
- `type` = Art des Eingabefeldes (`text`, `number`, `date`, etc.)

---

## Input Typen
- `type="text"` = normaler Text
- `type="number"` = nur Zahlen
- `type="date"` = Datumsauswahl

---

## Tabellen

```html
<table>
    <thead>                        <!-- Kopfzeile mit Spaltenüberschriften -->
        <tr>                       <!-- tr = table row = eine Zeile -->
            <th>Spalte 1</th>      <!-- th = table header = Überschrift -->
            <th>Spalte 2</th>
        </tr>
    </thead>
    <tbody>                        <!-- Inhalt der Tabelle -->
        <tr>                       <!-- eine Datenzeile -->
            <td>Wert 1</td>        <!-- td = table data = eine Zelle -->
            <td>Wert 2</td>
        </tr>
    </tbody>
</table>
```

### Elemente
- `<table>` = die gesamte Tabelle
- `<thead>` = Kopfbereich (Überschriften)
- `<tbody>` = Inhaltsbereich (Daten)
- `<tr>` = eine Zeile
- `<th>` = eine Überschriften-Zelle
- `<td>` = eine Daten-Zelle

### Mit Jinja2 Schleife
```html
<tbody>
    {% for eintrag in eintraege %}
    <tr>
        <td>{{ eintrag.item_name }}</td>
        <td>{{ eintrag.item_quantity }}</td>
    </tr>
    {% endfor %}
</tbody>
```
Für jeden Eintrag in der Datenbank → eine neue Zeile in der Tabelle.


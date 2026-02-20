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


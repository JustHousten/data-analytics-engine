# Python Dokumentation

---

## pip
Unter Windows funktioniert `pip` nicht direkt. Stattdessen:

```
python -m pip install paketname     → Paket installieren
python -m pip freeze > requirements.txt  → requirements erstellen/updaten
```

**Hinweis:** `pip freeze > requirements.txt` überschreibt die Datei jedes Mal komplett - derselbe Befehl zum Erstellen und Updaten!

---

## Packages / Module importieren

```python
from flask import Flask, render_template    # Einzelne Dinge importieren
import datetime                             # Ganzes Modul importieren
```


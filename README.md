Grenzenlose Intelligenz: Die klügsten Menschen der Erde

## Projektübersicht

Dieses Projekt zielt darauf ab, die Menschen mit den höchsten IQs aufzulisten, die jemals gelebt haben. Mithilfe dieser Applikation kannst du Personen nach verschiedenen Kriterien wie Land, Fachgebiet und IQ filtern. Die Applikation bietet auch eine benutzerfreundliche grafische Benutzeroberfläche (GUI) und ermöglicht eine Vielzahl von Analysen.

## Funktionen der Applikation

- **Filter nach Land**: Zeige Personen basierend auf ihrem Herkunftsland an.
- **Sortierung nach IQ**: Sortiere Personen nach ihrem IQ-Wert.
- **Durchschnittlicher IQ pro Land**: Berechne den durchschnittlichen IQ für jedes Land.
- **Diagramme und Grafiken**: Visualisiere die IQ-Verteilung und andere Informationen.
- **Interaktive GUI**: Wähle Filter und Sortieroptionen über eine moderne, benutzerfreundliche Oberfläche.

## Anforderungen

Stelle sicher, dass du folgende Software installiert hast, bevor du das Projekt ausführst:

- Python 3.x
- **PyQt5** (für das GUI)
- **pandas** (für die Datenverarbeitung)
- **matplotlib** (für die Diagramme)

Du kannst die benötigten Bibliotheken durch folgenden Befehl installieren:

```bash
pip install -r requirements.txt
```

Falls die `requirements.txt` nicht vorhanden ist, kannst du die folgenden Pakete einzeln installieren:

```bash
pip install PyQt5 pandas matplotlib
```

## Installation und Ausführung

1. **Projekt klonen oder herunterladen:**
   Lade das Projekt entweder als ZIP herunter oder klone es von deinem Repository:

   ```bash
   git clone <repository-url>
   ```
2. **Navigiere zum Projektverzeichnis:**

   ```bash
   cd intelligent_people_app
   ```
3. **Daten laden:**
   Stelle sicher, dass der Datensatz im Ordner `data/` liegt. Alternativ passe den Dateipfad in `data_loader.py` an.
4. **Das Programm ausführen:**
   Starte die Anwendung mit dem folgenden Befehl:

   ```bash
   python main.py
   ```
5. **GUI verwenden:**
   Im GUI kannst du Daten filtern, sortieren und Diagramme anzeigen lassen. Verwende die Dropdown-Menüs und Buttons, um die gewünschten Analysen durchzuführen.

## Projektstruktur

Das Projekt ist wie folgt strukturiert:

```plaintext
intelligent_people_app/
│
├── data/
│   └── data_loader.py      # Lädt den Datensatz und erstellt die Person-Objekte
├── models/
│   └── person.py           # Die Person-Klasse
├── analysis/
│   └── data_processor.py   # Datenanalyse und -verarbeitung
├── ui/
│   ├── main_window.py      # GUI-Hauptfenster
│   └── visualizer.py       # Grafiken/Diagramme
├── tests/
│   ├── test_data.py        # Tests für die Datenverarbeitung
│   └── test_ui.py          # Tests für das GUI
└── main.py                 # Der Einstiegspunkt des Programms
```

## Beispielnutzung

Nach dem Start der Anwendung wird eine moderne GUI angezeigt, mit der du verschiedene Daten analysieren kannst:

1. **Filter nach Land**:
   Wähle ein Land aus dem Dropdown-Menü, um Personen aus diesem Land anzuzeigen.
2. **Sortieren nach IQ**:
   Sortiere die Liste der Personen nach aufsteigendem oder absteigendem IQ.
3. **Durchschnittlicher IQ pro Land**:
   Visualisiere den durchschnittlichen IQ für verschiedene Länder als Diagramm.

## Tests

Um die Unit-Tests auszuführen und sicherzustellen, dass alles korrekt funktioniert, verwende den folgenden Befehl:

```bash
python -m unittest discover tests
```

Die Tests überprüfen die Filter- und Sortierfunktionen sowie die Berechnung des durchschnittlichen IQs pro Land.

## Weiterentwicklung

Wenn du das Projekt erweitern möchtest, kannst du z. B. folgende Funktionen hinzufügen:

- Mehr Analyseoptionen wie die Korrelation zwischen IQ und Auszeichnungen.
- Erweiterung der GUI um zusätzliche Filteroptionen.
- Weitere Visualisierungen und Diagramme für tiefere Einblicke in die Daten.

## Autor(en)

- Kaya Senay
- Rigani Jegatheeswaran

## Lizenz

Dieses Projekt steht unter keiner spezifischen Lizenz. Bitte kontaktiere die Autoren, falls du es weiterverwenden möchtest.

## Danksagung

Besonderer Dank geht an unseren Lehrer Dieter Kopp für die Unterstützung bei diesem Projekt.

```

### Hinweise:
- **Installation und Ausführung**: In der Beschreibung ist angegeben, wie das Programm gestartet wird. Hier kannst du auch den genauen Dateipfad für die Datenquelle angeben, falls dies notwendig ist.
- **Tests**: Hier sind auch Hinweise zur Durchführung der Unit-Tests enthalten, was für den reibungslosen Ablauf und das Debugging nützlich ist.

Du kannst diese Datei als `README.md` in dein Hauptverzeichnis legen. Wenn du noch Anpassungen oder Erweiterungen brauchst, lass es mich wissen!
```

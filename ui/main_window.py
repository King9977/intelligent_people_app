# ui/main_window.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QHBoxLayout
from analysis.data_processor import DataProcessor
from ui.visualizer import Visualizer

class MainWindow(QMainWindow):
    def __init__(self, processor):
        super().__init__()
        
        self.processor = processor
        self.init_ui()
    
    def init_ui(self):
        # Fenster-Einstellungen
        self.setWindowTitle("Grenzenlose Intelligenz - Die klügsten Menschen der Erde")
        self.setGeometry(100, 100, 1000, 800)

        # Haupt-Widget
        widget = QWidget()
        layout = QVBoxLayout()

        # Titel
        title_label = QLabel("Die klügsten Menschen der Welt", self)
        layout.addWidget(title_label)

        # Filter nach Land und Fachgebiet (Dropdown-Menüs)
        filter_layout = QHBoxLayout()

        # Filter nach Land
        self.country_combo = QComboBox(self)
        self.country_combo.addItem("Alle Länder")
        for person in self.processor.persons:
            if person.country not in [self.country_combo.itemText(i) for i in range(self.country_combo.count())]:
                self.country_combo.addItem(person.country)
        self.country_combo.currentIndexChanged.connect(self.update_table)
        filter_layout.addWidget(QLabel("Filter nach Land:"))
        filter_layout.addWidget(self.country_combo)

        # Filter nach Fachgebiet
        self.expertise_combo = QComboBox(self)
        self.expertise_combo.addItem("Alle Fachgebiete")
        for person in self.processor.persons:
            if person.field_of_expertise not in [self.expertise_combo.itemText(i) for i in range(self.expertise_combo.count())]:
                self.expertise_combo.addItem(person.field_of_expertise)
        self.expertise_combo.currentIndexChanged.connect(self.update_table)
        filter_layout.addWidget(QLabel("Filter nach Fachgebiet:"))
        filter_layout.addWidget(self.expertise_combo)

        layout.addLayout(filter_layout)

        # Sortierung nach IQ (Button)
        self.sort_button = QPushButton("Sortiere nach IQ", self)
        self.sort_button.clicked.connect(self.sort_by_iq)
        layout.addWidget(self.sort_button)

        # Diagrammanzeige-Button
        self.chart_button = QPushButton("Zeige IQ-Verteilung", self)
        self.chart_button.clicked.connect(self.show_iq_distribution)
        layout.addWidget(self.chart_button)

        # Tabelle zur Anzeige der Personen
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Land", "IQ", "Geburtsjahr"])
        layout.addWidget(self.table)

        # Haupt-Layout setzen
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Tabelle initial befüllen
        self.update_table()

    def update_table(self):
        """
        Aktualisiert die Tabelle basierend auf der aktuellen Filterung nach Land und Fachgebiet.
        """
        selected_country = self.country_combo.currentText()
        selected_expertise = self.expertise_combo.currentText()
        persons = self.processor.persons

        # Filter nach Land und Fachgebiet anwenden
        if selected_country != "Alle Länder":
            persons = self.processor.filter_by_country(selected_country)
        if selected_expertise != "Alle Fachgebiete":
            persons = self.processor.filter_by_expertise(selected_expertise)

        # Tabelle leeren
        self.table.setRowCount(0)
        
        # Neue Zeilen hinzufügen
        for i, person in enumerate(persons):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(person.name))
            self.table.setItem(i, 1, QTableWidgetItem(person.country))
            self.table.setItem(i, 2, QTableWidgetItem(str(person.iq)))
            self.table.setItem(i, 3, QTableWidgetItem(str(person.birth_year)))

    def sort_by_iq(self):
        """
        Sortiert die Personen nach IQ und aktualisiert die Tabelle.
        """
        persons = self.processor.sort_by_iq()
        self.processor.persons = persons  # Personen neu setzen nach Sortierung
        self.update_table()

    def show_iq_distribution(self):
        """
        Zeigt ein Diagramm der IQ-Verteilung an.
        """
        Visualizer.plot_iq_distribution(self.processor.persons)


def run_gui(processor):
    app = QApplication(sys.argv)
    main_window = MainWindow(processor)
    main_window.show()
    sys.exit(app.exec_())

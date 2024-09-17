import unittest
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from analysis.data_processor import DataProcessor
from models.person import Person

class TestMainWindow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # QApplication ist nötig für GUI-Tests
        cls.app = QApplication([])

    def setUp(self):
        persons = [
            Person("Person A", "Germany", "Physics", 180, "Nobel Prize", 1900, "Male", "Theory A", "Award A", "PhD", "High"),
            Person("Person B", "USA", "Math", 150, "Field Medal", 1910, "Female", "Theory B", "Award B", "Master", "Moderate"),
        ]
        processor = DataProcessor(persons)
        self.window = MainWindow(processor)

    def test_table_population(self):
        """
        Testet, ob die Tabelle korrekt mit den Personendaten gefüllt wird.
        """
        self.window.update_table()
        self.assertEqual(self.window.table.rowCount(), 2)
        self.assertEqual(self.window.table.item(0, 0).text(), "Person A")
        self.assertEqual(self.window.table.item(1, 0).text(), "Person B")

    def test_filter_by_country(self):
        """
        Testet das Filtern der Personen nach Land über das GUI.
        """
        self.window.country_combo.setCurrentText("Germany")
        self.window.update_table()
        self.assertEqual(self.window.table.rowCount(), 1)
        self.assertEqual(self.window.table.item(0, 0).text(), "Person A")

    def test_sort_by_iq_button(self):
        """
        Testet, ob der Button zum Sortieren nach IQ korrekt funktioniert.
        """
        self.window.sort_button.click()
        self.assertEqual(self.window.table.item(0, 0).text(), "Person A")  # Highest IQ should be first

if __name__ == '__main__':
    unittest.main()

import unittest
from models.person import Person
from analysis.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.persons = [
            Person("Person A", "Germany", "Physics", 180, "Nobel Prize", 1900, "Male", "Theory A", "Award A", "PhD", "High"),
            Person("Person B", "Germany", "Math", 150, "Field Medal", 1910, "Female", "Theory B", "Award B", "Master", "Moderate"),
            Person("Person C", "USA", "Physics", 170, "Nobel Prize", 1920, "Male", "Theory C", "Award C", "Bachelor", "Low"),
            Person("Person D", "France", "Literature", 140, "Pulitzer Prize", 1930, "Female", "Book D", "Award D", "PhD", "High")
        ]
        self.processor = DataProcessor(self.persons)

    def test_filter_by_country(self):
        filtered_persons = self.processor.filter_by_country("Germany")
        self.assertEqual(len(filtered_persons), 2)
        self.assertEqual(filtered_persons[0].name, "Person A")
        self.assertEqual(filtered_persons[1].name, "Person B")

    def test_filter_by_expertise(self):
        filtered_persons = self.processor.filter_by_expertise("Physics")
        self.assertEqual(len(filtered_persons), 2)
        self.assertEqual(filtered_persons[0].name, "Person A")
        self.assertEqual(filtered_persons[1].name, "Person C")

    def test_sort_by_iq(self):
        sorted_persons = self.processor.sort_by_iq()
        self.assertEqual(sorted_persons[0].name, "Person A")
        self.assertEqual(sorted_persons[-1].name, "Person D")

    def test_average_iq_per_country(self):
        avg_iq = self.processor.average_iq_per_country()
        self.assertAlmostEqual(avg_iq["Germany"], 165)
        self.assertAlmostEqual(avg_iq["USA"], 170)
        self.assertAlmostEqual(avg_iq["France"], 140)

if __name__ == '__main__':
    unittest.main()

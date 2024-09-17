import pandas as pd
from models.person import Person

class DataLoader:
    @staticmethod
    def load_data(file_path='C:/Users/kaya.senay/Desktop/Schule/Lehrjahr3/Modul 323/intelligent_people_app/data/top_intelligent_people_in_the_world_5000.csv'):
        """
        Lädt den Datensatz aus einer CSV-Datei und gibt eine Liste von Person-Objekten zurück.
        :param file_path: Pfad zur CSV-Datei
        :return: Liste von Person-Objekten
        """
        try:
            data = pd.read_csv(file_path)
            persons = []
            
            for _, row in data.iterrows():
                person = Person(
                    name=row['Name'],
                    country=row['Country'],
                    field_of_expertise=row['Field of Expertise'],
                    iq=row['IQ'],
                    achievements=row['Achievements'],
                    birth_year=row['Birth Year'],
                    gender=row['Gender'],
                    notable_works=row['Notable Works'],
                    awards=row['Awards'],
                    education=row['Education'],
                    influence=row['Influence']
                )
                persons.append(person)

            print(f"{len(persons)} Personen erfolgreich geladen.")
            return persons
        except FileNotFoundError:
            print(f"Datei nicht gefunden: {file_path}")
            return []

class DataProcessor:
    def __init__(self, persons):
        self.persons = persons

    def filter_by_country(self, country):
        """
        Filtert Personen nach ihrem Herkunftsland.
        """
        return [person for person in self.persons if person.country == country]

    def filter_by_expertise(self, expertise):
        """
        Filtert Personen nach ihrem Fachgebiet.
        """
        return [person for person in self.persons if person.field_of_expertise == expertise]

    def sort_by_iq(self, descending=True):
        """
        Sortiert die Personenliste nach IQ in absteigender Reihenfolge.
        """
        return sorted(self.persons, key=lambda person: person.iq, reverse=descending)

    def average_iq_per_country(self):
        """
        Berechnet den durchschnittlichen IQ pro Land.
        """
        iq_by_country = {}
        for person in self.persons:
            if person.country not in iq_by_country:
                iq_by_country[person.country] = []
            iq_by_country[person.country].append(person.iq)

        avg_iq_by_country = {country: sum(iqs) / len(iqs) for country, iqs in iq_by_country.items()}
        return avg_iq_by_country

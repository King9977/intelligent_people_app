# ui/visualizer.py

import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_iq_distribution(persons):
        """
        Zeigt ein Balkendiagramm, das die IQ-Verteilung darstellt.
        """
        countries = {}
        
        for person in persons:
            if person.country in countries:
                countries[person.country].append(person.iq)
            else:
                countries[person.country] = [person.iq]
        
        # Durchschnittlicher IQ pro Land berechnen
        avg_iq_per_country = {country: sum(iqs) / len(iqs) for country, iqs in countries.items()}
        
        # Diagramm erstellen
        plt.figure(figsize=(10, 6))
        plt.bar(avg_iq_per_country.keys(), avg_iq_per_country.values(), color='skyblue')
        plt.xlabel('Land')
        plt.ylabel('Durchschnittlicher IQ')
        plt.title('Durchschnittlicher IQ pro Land')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

class Person:
    def __init__(self, name, country, field_of_expertise, iq, achievements, birth_year, gender, notable_works, awards, education, influence):
        self.name = name
        self.country = country
        self.field_of_expertise = field_of_expertise
        self.iq = iq
        self.achievements = achievements
        self.birth_year = birth_year
        self.gender = gender
        self.notable_works = notable_works
        self.awards = awards
        self.education = education
        self.influence = influence

    def __str__(self):
        return f'{self.name} ({self.country}, {self.field_of_expertise}) - IQ: {self.iq}'

class car:
    def __init__(self, mileage, year, make, model) -> None:
        self.mileage = mileage
        self.year = year
        self.make = make
        self.model = model

    def age(self, curr_year):
        return curr_year - self.year

        
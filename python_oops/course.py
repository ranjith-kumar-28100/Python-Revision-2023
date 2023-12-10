class Course:
    def __init__(self, name, cost, ratings):
        self.name = name
        self.cost = cost
        self.ratings = ratings

    def average(self):
        return sum(self.ratings) / len(self.ratings)


c1 = Course("Python for Beginners", 899, [4.5, 5, 3.3, 1.0, 0, 2.5, 5, 5, 5, 5, 5])
c2 = Course(name="NumPy for Data Analysis", cost=500, ratings=[5, 4.5, 3, 4.5, 5])
print(c1.name, c1.cost, c1.ratings)
print(c2.name, c2.cost, c2.ratings)
print(c1.average())
print(c2.average())

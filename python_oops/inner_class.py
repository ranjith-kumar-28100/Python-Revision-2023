class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print(f"Engine: {self.number} started")


c1 = Car("BenZ", 2023)
e1 = c1.Engine(989898)
e1.start()

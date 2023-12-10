class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):
    def __init__(self, cruise_control_enabled, make, model, year):
        # BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.cruise_control_enabled = cruise_control_enabled

    def start(self):
        super().start()
        print("3 Series Special Start-up")


class FiveSeries(BMW):
    def __init__(self, parking_assist_enabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parking_assist_enabled = parking_assist_enabled


obj = ThreeSeries(True, 'BMW', '3Series', 2023)
print(obj.make, obj.model, obj.year, obj.cruise_control_enabled)
obj.start()
obj.stop()
obj2 = FiveSeries(True, 'BMW', '5Series', 2024)
print(obj2.make, obj2.model, obj2.year, obj2.parking_assist_enabled)
obj2.start()
obj2.stop()

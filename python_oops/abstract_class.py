from abc import ABC, abstractmethod


class BMW(ABC):
    @abstractmethod
    def drive(self):
        pass

    def start(self):
        print("BMW Started")

    def stop(self):
        print("BMW Stopped")


class ThreeSeries(BMW):
    def drive(self):
        print("Three Series is on Driving mode")


c1 = ThreeSeries()
c1.start()
c1.stop()
c1.drive()

from abc import ABC, abstractmethod


class BMW(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ThreeSeries(BMW):
    def drive(self):
        print("Three Series is on Driving mode")

    def start(self):
        print("Three Series Started")

    def stop(self):
        print("Three Series Stopped")


c1 = ThreeSeries()
c1.start()
c1.stop()
c1.drive()

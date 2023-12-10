class Flight:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()


class TypeAEngine:
    def start(self):
        print("Starting Type A Engine")


class TypeBEngine:
    def start(self):
        print("Starting Type B Engine")


e1 = TypeAEngine()
e2 = TypeBEngine()
f1 = Flight(e1)
f1.start_engine()
f2 = Flight(e2)
f2.start_engine()

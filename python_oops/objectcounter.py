class ObjectCounter:
    numOfObjects = 0

    def __init__(self):
        ObjectCounter.numOfObjects += 1

    @staticmethod
    def display_count():
        print(f"No. of objects created = {ObjectCounter.numOfObjects}")


oc1 = ObjectCounter()
oc2 = ObjectCounter()
oc3 = ObjectCounter()
ObjectCounter.display_count()

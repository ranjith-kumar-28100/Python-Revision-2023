class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setClinical(self, clinical):
        self.clinical = clinical

    def getClinical(self):
        return self.clinical

    def add_clinical_data(self, clinical):
        self.clinical.append(clinical)


class Clinical:
    def __init__(self, component_name, component_value):
        self.component_name = component_name
        self.component_value = component_value

    def setComponent_name(self, component_name):
        self.component_name = component_name

    def getComponent_name(self):
        return self.component_name

    def setComponent_value(self, component_value):
        self.component_value = component_value

    def getComponent_value(self):
        return self.component_value


p1 = Patient("Ajith Kumar", 51)
c1 = Clinical("Blood Group", "B-ve")
p1.add_clinical_data(c1)
print(p1.getName(), p1.getAge())
c2 = Clinical("Sugar Level", "High")
p1.add_clinical_data(c2)
for data in p1.getClinical():
    print(data.getComponent_name(), ':', data.getComponent_value())

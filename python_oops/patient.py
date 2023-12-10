class Patient:
    def __init__(self, id, name, ssn):
        self.__id = id
        self.__name = name
        self.__ssn = ssn

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn):
        self.__ssn = ssn


p = Patient(1, "Thala Ajith", 1122334455)
p.id = 5
p.name = "AK"
p.ssn = 112233445599
print(p.id)
print(p.name)
print(p.ssn)

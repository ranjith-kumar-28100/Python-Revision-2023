class Student:
    def setId(self, id):
        print("Setter for id")
        self.__id = id

    def getId(self):
        print("Getter for id")
        return self.__id

    id = property(getId, setId, None)

    def setName(self, name):
        print("Setter for name")
        self.__name = name

    def getName(self):
        print("Getter for name")
        return self.__name

    name = property(getName, setName, None)

    @property
    def age(self):
        print("Getter for Age")
        return self.__age

    @age.setter
    def age(self, age):
        print("Setter for Age")
        self.__age = age


s = Student()
s.setId(5)
s.setName('RKG')
print(s.getId())
print(s.getName())
s1 = Student()
s1.id = 10
print(s1.id)
s1.name = "RPKN"
print(s1.name)
s1.age = 23
print(s1.age)

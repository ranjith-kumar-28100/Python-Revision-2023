class Programmer:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechSkills(self, tech_skills):
        self.tech_skills = tech_skills

    def getTechSkills(self):
        return self.tech_skills


p1 = Programmer()
p1.setName("Ranjith Kumar")
p1.setSalary(1_25_000)
p1.setTechSkills("Python, Machine Learning, Deep Learning")
print(p1.getName(), p1.getSalary(), p1.getTechSkills())

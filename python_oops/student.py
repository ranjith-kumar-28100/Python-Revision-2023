class Student:
    major = "CSE"

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name


s1 = Student(1, "Ranjith Kumar G")
s2 = Student(2, "Anurag Pandey")
s3 = Student(3, "V Lahari")
print(s1.major, s2.major, s3.major, Student.major)

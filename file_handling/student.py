class Student:
    def __init__(self,roll_no,name,std):
        self.__roll_no = roll_no
        self.__name = name
        self.__std = std

    @property
    def roll_no(self):
        return self.__roll_no

    @roll_no.setter
    def roll_no(self,roll_no):
        self.__roll_no=roll_no

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def std(self):
        return self.__std

    @std.setter
    def std(self,std):
        self.__std=std

    def display(self):
        print( f"roll_no: {self.roll_no}, name: {self.name}, standard: {self.std}")

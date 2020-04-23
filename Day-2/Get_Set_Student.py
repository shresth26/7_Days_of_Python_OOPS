class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

    def getRollNumber(self):
        return self.__RollNumber

detail = Student()
detail.setName("Mohit")
print("The student name is", detail.getName())
detail.setRollNumber(69)
print("The student roll number is", detail.getRollNumber())

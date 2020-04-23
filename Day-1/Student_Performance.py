class Student:
    def __init__(self, name = "", phy = 0, chem = 0, bio = 0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio
    def percentage(self):
        return (self.totalObtained()/ 300) * 100

obj = Student("Mark", 70 , 80, 90)
print(obj.percentage())

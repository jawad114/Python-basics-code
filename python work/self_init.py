class school():
     leave = 9
     def __init__(self, aname, asalary, aroll):
         self.name = aname
         self.salary = asalary
         self.roll = aroll
     def detail(self):
         return f"My name is {self.name}, \n Roll No:{self.Roll_No} , \n Roll:{self.Roll} "
     def test(cls, null):
         # param = null.split("-")
         # return cls(param[0], param[1], param[2])
           return cls(*null.split("-"))

khan = school("Jawad Shah", 234554345, "Student")
shah = school.test("JawadShah-76556-Noooooo")

# khan.name = "Jawad Shah"
# khan.Roll_No = 2347
# khan.Roll = "Student"
print(khan.name)
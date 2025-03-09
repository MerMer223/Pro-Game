class Student():
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def printdetails(self):
        print(self.name,self.age,self.hobby)
    def changedetails(self):
        print(1,2,3)
        choice = int(input("type 1 to change name type 2 to change age type 3 to change hobby"))
        if choice == 1:
            self.name = input("Enter new name")
        elif choice == 2:
            self.age = input("Enter new age")
        elif choice == 3:
            self.hobby = input("Enter new hobby")



s1 = Student("Mehraab",13,"Basketball")
s1.printdetails()

s2 = Student("Brady",14,"Video Games")
s2.printdetails()

s3 = Student("Yassin",13,"Shopping")
s3.printdetails()
s3.changedetails()


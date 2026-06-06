class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def display(self):
        print(f"{self.name} is in grade {self.grade}")


s1=Student("kamaraj",90)
s2=Student("Lingesh",99)
s3=Student("Mani",100)
s4=Student("Rai",100)

s1.display()
s2.display()
s3.display()
s4.display()
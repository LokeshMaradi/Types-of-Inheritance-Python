class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)
class teacher(person):
    def __init__(self,name,age,exp,r_area):
        person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def displaydata(self):
        person.display(self)
        print("EXPERIENCE:",self.exp)
        print("RESEARCH AREA:",self.r_area)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print("COURSE:",self.course)
        print("MARKS:",self.marks)
print("TEACHER")
T=teacher("jaya",43,20,"recommender systems")
T.displaydata()
print("STUDENT")
S=student("mani",20,"btech",78)
S.displaydata()

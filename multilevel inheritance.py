class person:
    def name(self):
        print("name")
class teacher(person):
    def qualification(self):
        print("qualification ph d must")
class HOD(teacher):
    def experience(self):
        print("experience atleast 15 years")
hod=HOD()
hod.name()
hod.qualification()
hod.experience()

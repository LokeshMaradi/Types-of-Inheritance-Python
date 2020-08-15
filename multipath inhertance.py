class student:
    def name(self):
        print("name")
class academic_performance(student):
    def acad_score(self):
        print("academic score 90 percent and above")
class CSE(student):
    def CSE_score(self):
        print("CSE score 60 per and above")
class result(academic_performance,ECA):
    def eligibility(self):
        print("minimum eligibility to apply")
        self.acad_score()
        self.CSE_score()
R=result()
R.eligibility()

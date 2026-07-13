#day 6 deals with OOP and to exercise ill stick to the school and grades example

class Students:

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def rating(self):
        if self.grade <=2:
            return "very good"
        
        elif self.grade ==3:
            return "good"
        
        elif self.grade ==4:
            return "okay"
        
        else:
            return "bad"
        
    def subjct(self):
        return self.subject
        
        

student_1 = Students("Mustapha", 5, "maths")
student_2 = Students("Jenny", 1, "maths")

print(student_2.subjct())

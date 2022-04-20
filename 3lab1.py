 
class SRMIST:
    school = "SRMIST"
    dept1 = "Computer Science"
    dept2 = "Electronics"
    dept3 = "Mechanical"

    def __init__(self,specialization = "Electronics"):
        self.specialization = specialization 
        print("School: ", self.school)
        print("Department 1: ", self.dept1)
        print("Department 2: ", self.dept2)
        print("Department 3: ", self.dept3)
        print("Specialization: ", self.specialization)

    def remove_dept(self):
        self.dept1 = ""
        self.dept2 = ""
        print("School: ", self.school)
        print("Department 1: ", self.dept1)
        print("Department 2: ", self.dept2)
        print("Department 3: ", self.dept3)
        print("Specialization: ", self.specialization)

srmist = SRMIST("CTECH")
srmist.remove_dept()
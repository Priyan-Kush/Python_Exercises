class Dept:
    def __init__(self, name = "SCO"):
        self.name = name
    def __str__(self):
        return self.name
dept1 = Dept()
dept2 = Dept("ECE")
# print(dept1)
print(dept2)
print(dept1.name)
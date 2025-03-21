class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self.__bonus = 50000

    def display(self):
        # print ("Name:", self.name, ", Salary:", self._salary)
        return f"Name: {self.name}, Salary: {self._salary}"
    
    def displayBonus(self):
        return ("Bonus:", self.__bonus)

e = Employee("John", 10000)
print(e.display())
print(e._Employee__bonus)

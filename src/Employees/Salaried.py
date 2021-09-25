from Employees.Employee import Employee

class Salaried(Employee):
    def __init__(self, name, rg, id, adress, sindMember, wage, paymentMethod, date):
        super().__init__(name, rg, id, adress, sindMember, paymentMethod, date)
        self.wage = wage
        self.payDate = "monthly-$"

    def get_wage(self):
        return self.wage
    def set_wage(self, value):
        self.wage = value

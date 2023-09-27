"""Employee pay calculator."""

class Employee:
    def __init__(self, name, salary, hours_worked, hourly_rate, flat_commission, contract_count, contract_rate):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.flat_commission = flat_commission
        self.contract_count = contract_count
        self.contract_rate = contract_rate

    def get_pay(self):
        return (self.salary + (self.hours_worked * self.hourly_rate) + self.flat_commission + (self.contract_count * self.contract_rate))

    def __str__(self):
        # 6 categories to split into
        if (self.salary > 0):
            base_text = "monthly salary of "+str(self.salary)
        else:
            base_text = "contract of "+str(self.hours_worked)+" hours at "+str(self.hourly_rate)+"/hour"
        if (self.flat_commission > 0):
            commission_text = " and receives a bonus commission of "+str(self.flat_commission)+"." #receive bonus commission
        elif (self.contract_count > 0):
            commission_text = " and receives a commission for "+str(self.contract_count)+" contract(s) at "+str(self.contract_rate)+"/contract." #receive contract commission
        else:   #receive no commission
            commission_text = "."
        
        return (f"{self.name} works on a {base_text}{commission_text} Their total pay is {str(self.get_pay())}.")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,0,0,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,100,25,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,0,0,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,150,25,0,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,0,0,1500,0,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,120,30,600,0,0)
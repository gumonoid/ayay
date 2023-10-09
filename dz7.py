#завдання 1

def generator_func():
    for i in range(5):
        yield i

class Iteratorwithgenerator:
    def __init__(self):
        self.generator = generator_func()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

iterator = Iteratorwithgenerator()

for n in iterator:
    print(n)


#додаткове завдання

class Student:
    def __init__(self, name, age, money=0):
        self.name = name
        self.age = age
        self.money = money
        self.days_passed = 0

    def earn_money(self, amount):
        if amount > 0:
            self.money += amount
            return f"{self.name} заробив {amount} грошей. загальна сума грошей: {self.money}"
        else:
            return "Сума заробітку повинна бути більше нуля"

    def spend_money(self, amount):
        if amount > 0 and amount <= self.money:
            self.money -= amount
            return f"{self.name} витратив {amount} грошей. залишилось грошей: {self.money}"
        elif amount > self.money:
            return f"{self.name} не має достатньо грошей для цієї витрати."
        else:
            return "Сума витрат повинна бути більше нуля."

    def relax(self, hours):
        if hours <= 0:
            return "Час відпочинку повинен бути більше нуля."

        if self.money < hours * 10:
            return f"{self.name} не може дозволити собі {hours} годин відпочинку."

        self.spend_money(hours * 10)
        return f"{self.name} відпочив {hours} годин."

    def __iter__(self):
        return self

    def __next__(self):
        if self.days_passed < self.age:
            self.days_passed += 1
            return f"День {self.days_passed}: {self.earn_money(20)}, {self.spend_money(10)}, {self.relax(2)}"
        else:
            raise StopIteration


student1 = Student("Ілля", 20, 100)


for day_info in student1:
    print(day_info)

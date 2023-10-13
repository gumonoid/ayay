#завдання 1

import random
import logging

# Налаштування логування
logging.basicConfig(filename='simulation.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('simulation')

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Auto:
    stats = {
        'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
        'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choice(list(Auto.stats))
        self.fuel = Auto.stats[self.brand]['fuel']
        self.strength = Auto.stats[self.brand]['strength']
        self.consumption = Auto.stats[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            logger.info('The car cannot go')
            return False

class Job:
    stats = {
        'Java developer': {'salary': 50, 'gladness_less': 10},
        'Python developer': {'salary': 40, 'gladness_less': 3},
        'C++ developer': {'salary': 45, 'gladness_less': 25},
        'Rust developer': {'salary': 70, 'gladness_less': 1},
    }

    def __init__(self):
        self.job = random.choice(list(Job.stats))
        self.salary = Job.stats[self.job]['salary']
        self.gladness_less = Job.stats[self.job]['gladness_less']

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
            logger.info(f"{self.name} is fed and happier now.")
        else:
            logger.info(f"{self.name} is not hungry right now.")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            self.hunger += 5
            logger.info(f"{self.name} is having fun and getting happier.")
        else:
            logger.info(f"{self.name} is already very happy.")

    def pet_status(self):
        logger.info(f"{self.name} ({self.species}) status:")
        logger.info(f"Happiness: {self.happiness}")
        logger.info(f"Hunger: {self.hunger}")

    def is_alive(self):
        if self.happiness <= 0:
            logger.info(f"{self.name} is too unhappy and has run away.")
            return False
        elif self.hunger >= 100:
            logger.info(f"{self.name} has starved to death.")
            return False
        else:
            return True

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto()

    def get_job(self):
        if not self.car.drive():
            self.to_repair()
            return
        self.job = Job()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            nick_pet.feed()

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logger.info('Car repaired')

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            logger.info('Bought fuel!')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            logger.info('Bought food!')
            self.money -= 50
            self.home.food += 50
        elif manage == 'sweets':
            logger.info('Yummy!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logger.info('Chilling')

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logger.info('Home cleaned')

    def days_indexes(self, day):
        day_str = f"Today is the {day} day of {self.name}'s life"
        logger.info(f"{day_str:=^50}")
        human_indexes = f"{self.name}'s indexes"
        logger.info(f"{human_indexes:^50}")
        logger.info('money: %d', self.money)
        logger.info('satiety: %d', self.satiety)
        logger.info('gladness: %d', self.gladness)
        home_indexes = 'Home indexes'
        logger.info(f"{home_indexes:^50}")
        logger.info('food: %d', self.home.food)
        logger.info('mess: %d', self.home.mess)
        car_indexes = f"{self.car.brand} car indexes"
        logger.info(f"{car_indexes:^50}")
        logger.info('fuel: %d', self.car.fuel)
        logger.info('strength: %d', self.car.strength)

    def is_alive(self):
        if self.gladness < 0:
            logger.info('Depression')
            return False
        elif self.satiety < 0:
            logger.info('Hunger death')
            return False
        elif self.money < -500:
            logger.info('Bankrupt')
            return False
        else:
            return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            logger.info('Settled in the house')
            self.get_home()
        if self.car is None:
            logger.info('Get a car')
            self.get_car()
        if self.job is None:
            logger.info('Get a job')
            self.get_job()
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            logger.info('Ill go to eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping(manage='sweets')
        return True

nick_pet = Pet(species='Dog', name='Buddy')
nick = Human(name='Nick')

for day in range(1, 365):
    if not nick.live(day):
        break

#завдання 2

import time

def m_time(func, arg, karg):
    start_time = time.time()
    result = func(arg, karg)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def s_function(x, y):
    time.sleep(2)
    return x + y

result, execution_time = m_time(s_function, 3, 4)
print(f"Результат: {result}")
print(f"Час виконання: {execution_time} секунд")


# class Student:
#     print("hi")
#     def __init__(self):
#         self.height = 160
#         print("i am alive")
#         print(self)
# first_student = Student()
# second_student = Student()
# third_student = Student()
#
# print(first_student.height)
# Student.__init__(first_student)


# class Student:
#     def __init__(self, height1=160):
#         self.height = height1
#
# nick = Student()
# ket = Student(height1=170)
# chiril = Student(height1=2833)
# print(nick.height)
# print(ket.height)
# print(chiril.height)

# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
# nick = Student()
# ket = Student(height=170)
# chiril = Student()
# print(nick.amount_of_students)
# print(ket.amount_of_students)


# class Student:
#     height = 160
#     def __init__(self):
#         print(self.height)
#         self.height += 10
# nick = Student()
# kate = Student()

# x=10
# class Locker:
#     print(x)
#     def func_1(self):
#         x=20
#         print(x)
#         def func_2():
#             print(x)
#         func_2()
# some_object = Locker()
# some_object.func_1()



# class Student:
#     amount_of_students = 0
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
# mick = Student()
# kate = Student(height=170)
# mick.grow(height=15)
# print(mick)
# print(kate)
# mick = Student()
# kate = Student()


# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         if self.name:
#             return f'eu saunt studentsi ma btumehbvf{self.name}.'
#         else:
#             return "eu sunt suryudent si nam u nujne"
# alice = Student(name = "alice")
# print(alice)
# unoun_stuent = Student()
# print(unoun_stuent)


# import random
# class Student():
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#     def to_study(self):
#         print("trebuie de invatat")
#         self.progress += 0.12
#         self.gladness -= 5
#     def to_sleep(self):
#         print("voi dormui alpweeppe")
#         self.gladness += 3
#     def to_chill(self):
#         print("timp de odihna")
#         self.gladness += 5
#         self.progress -= 0.1
#     def is_alive(self):
#         if self.progress < -0.5:
#
#             print("dead")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("deprehsihiefubebv")
#             self.alive = False
#         elif self.progress > 5:
#             print("o murit de fericire")
#             self.alive = False
#     def end_of_day(self):
#             print(f"fericire = {self.gladness}")
#             print(f"Progres = {round(self.progress, 2)}")
#     def live(self, day):
#         day = "ziua " + str(day) +" din viata lui" +self.name + " "
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
# iarik = Student(name="iarik")
# for day in range(365):
#     if iarik.alive == False:
#         break
#     iarik.live(day)











# class Human:
#     def __init__(self, name ="Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passenger(self, human):
#         self.passengers.append(human)
#     def print_passengers_name(self):
#         if self.passengers!= []:
#             print(f"In {self.brand} there are this passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"nu sut pasageri{self.brand}")
# nick = Human("Nick")
# iarik = Human("Iarik")
# car = Auto("mercedes")
# car.add_passenger(nick)
# car.add_passenger(iarik)
# car.print_passengers_name()


import random
# Define the House class
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
# Define the Auto class
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    # Method to simulate driving the car
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False
# Define the Job class
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]
# Define the Human class
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
    # Method to get a home
    def get_home(self):
        self.home = House()
    # Method to get a car
    def get_car(self):
        self.car = Auto(brands_of_car)
    # Method to get a job
    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()
            return
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")

            else:
                self.to_repair()
            return
    def shopping(self, manage):
        if self.car.drive():
            if manage == "fuel":
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
            return

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day}:=^50")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes}:^50", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes}:^50", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes}:^50", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the House")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess... \n So i will clean the House")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Let's start working ")
        elif dice == 3:
            print("cleaning time")
            self.clean_home()
        elif dice == 4:
            print("time for trets ")
            self.shopping(manage = "deliciase")
        return True
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},}
brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "bugati": {"fuel": 50, "strength": 40, "consumption": 10},
    "chiunisex": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},}

nick = Human(name="iarik")
for day in range(1, 8):
    print(f"Day {day}")
    if not nick.live(day):
        break














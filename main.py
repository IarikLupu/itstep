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


import random
class Student():
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("trebuie de invatat")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("voi dormui alpweeppe")
        self.gladness += 3
    def to_chill(self):
        print("timp de odihna")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:

            print("dead")
            self.alive = False
        elif self.gladness <= 0:
            print("deprehsihiefubebv")
            self.alive = False
        elif self.progress > 5:
            print("o murit de fericire")
            self.alive = False
    def end_of_day(self):
            print(f"fericire = {self.gladness}")
            print(f"Progres = {round(self.progress, 2)}")
    def live(self, day):
        day = "ziua " + str(day) +" din viata lui" +self.name + " "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
iarik = Student(name="iarik")
for day in range(365):
    if iarik.alive == False:
        break
    iarik.live(day)
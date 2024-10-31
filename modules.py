class RightTectangle:
    """Something"""
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_surface(self):
        return  self.height * self.width


class Triangle:
    """Something"""
    def __get__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return (self.c + self.b + self.a)

    def get_surface(self):
        p = self.c + self.b + self.a
        q = p/2
        s = (q*(q-self.a)*(q-self.b)*(q-self.c))**(1/2)
        return s

class Car():
    """Something"""
    def __init__(self, model, brand, date, technical, distance):
        self.model = model
        self.brand = brand
        self.date = date
        self.technical = technical
        self.distance = distance

    def add_distance(self, distance):
        return (self.distance + distance)

    def update_date(self, year):
        self.technical = year
        return self.technical


class City():
    """Something"""
    def __init__(self, name, surface, people):
        self.name = name
        self.surface = surface
        self.people = people

    def add_people(self, num):
        return self.people + num

class Group():
    """Something"""
    def __init__(self, name, *student):
        self.name = name
        self.student = student

    def get_student_number(self):
        return len(self.student)


class Animals():
    """Something"""
    def __init__(self, name, species, num_foot, food):
        self.name = name
        self.species = species
        self.num_foot = num_foot
        self.food = food


class House:
    """Something"""
    def __init__(self, num, electrical, air, water):
        self.num = num
        self.electrical = electrical
        self.air = air
        self.water = water

    def get_info(self):
        return f"Your flat: {self.num}\n Your electrical balans: {self.electrical}\n Your air balans: {self.air}\n Your water balans: {self.water}"


class Subject():
    """Something"""
    def __init__(self, name):
        self.name = name


class Student():
    """Something"""
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course

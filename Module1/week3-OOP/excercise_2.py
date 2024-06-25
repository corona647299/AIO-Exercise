from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass
    
    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name=name, yob=yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - yoB: {self._yob} - Grade: {self._grade}")


student1 = Student('Trung', 1998, 10)
student1.describe()


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name=name, yob=yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - yoB: {self._yob} - Specialist: {self._specialist}")


doctor1 = Doctor("Trung", 1992, "CDHA")
doctor1.describe()


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name=name, yob=yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - yoB: {self._yob} - Subject: {self._subject}")


teacher1 = Teacher("Trung", 1990, "toán")
teacher1.describe()

class Ward:
    def __init__(self, name):
        self._name = name
        self.__list_people = list()
        
    def add_person(self, person: Person):
        self.__list_people.append(person)
        
    def describe(self):
        print(f'Name: {self._name}')
        for p in self.__list_people:
            p.describe()
            
    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                counter += 1
        return counter
   
    def sort_yob(self):
        return self.__list_people.sort(key=lambda x: x.get_yob())
    
    def compute_average(self):
        counter = 0
        total = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                counter += 1
                total += p.get_yob()
        
        return total / counter
            
ward1 = Ward('ward1')
ward1.add_person(student1)
ward1.add_person(doctor1)
ward1.add_person(teacher1)
ward1.describe()

print(ward1.count_doctor())

ward1.sort_yob()
ward1.describe()

print(ward1.compute_average())
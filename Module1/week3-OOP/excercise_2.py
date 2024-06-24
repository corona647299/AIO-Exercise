from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob
    
    @abstractmethod
    def describe(self):
        pass
    
class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name=name, yob=yob) 
        self._grade = grade
        
    def describe(self):
        print(f"Student - Name: {self._name} - yoB: {self._yob} - Grande: {self._grade}")
        
student1 = Student('Trung', 1999, 10)
student1.describe()

class Dotor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name=name, yob=yob) 
        self._specialist = specialist
        
    def describe(self):
        print(f"Student - Name: {self._name} - yoB: {self._yob} - Specialist: {self._specialist}")
        
doctor1 = Doctor("Trung", 1992, "CDHA")
doctor1.describe()


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name=name, yob=yob) 
        self._subject = subject
        
    def describe(self):
        print(f"Student - Name: {self._name} - yoB: {self._yob} - Subject: {self._subject}")
        
teacher1 = Teacher("Trung", 1990, "toán")
teacher1.describe()

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []  
    
    def add_person(self, person):
        self.people.append(person)
    
    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            person.describe()
            
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    
    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    
    def sort_age(self):
        self.people.sort(key=lambda x: x.yob)
    
    def describe_sorted(self):
        self.sort_age()
        self.describe()

print("Danh sách được sắp xếp theo tuổi:")
ward.describe_sorted()


        
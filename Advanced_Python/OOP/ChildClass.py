class Person:
     def __init__(self,name,surname,age):
          self.name=name
          self.surname=surname
          self.age=age
        
          print("person sınıfı turetildi")

     def intro(Self):
          print(f"Selam Ben {Self.name} {Self.surname} {Self.age} yaşındayım")   



class Student(Person):
     def __init__(self, name, surname, age,number):
          #Person.__init__(self,name,surname,age)
          super().__init__(name,surname,age)
          self.number=number
          print("Student türetildi.")

     def study(self):
          print(f"{self.name} ders çalışıyor.")

     def intro(Self):
        print(Self.name,Self.surname,Self.age,Self.number)   


class Teacher(Person):
    def __init__(self, name, surname, age,branch):
         super().__init__(name, surname, age)
         self.branch=branch
         print("Teacher  türetildi.")

    def teach(self):
         print(f"{self.name} hoca {self.branch} dersini anlatıyor.")

p1=Person("Emre","Yenen",23)
p1.intro()

s1=Student("Enes","Yenen",24,105)
s1.intro()
# s1.study()
# print(s1.number)

t1=Teacher("Emree","Y",40,"fizik")
t1.intro()
# t1.teach()
# print(t1.branch)
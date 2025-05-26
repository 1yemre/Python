class Person:
     def __init__(self,name,surname,age):
          self.name=name
          self.surname=surname
          self.age=age
        
          print("person sınıfı turetildi")

     def intro(Self):
          print(f"Selam Ben {Self.name} {Self.surname} {Self.age} yaşındayım")   



class Student(Person):
     pass


class Teacher(Person):
    pass



p1=Person("Emre","Yenen",23)
p1.intro()

s1=Student("Enes","Yenen",24)
s1.intro()


t1=Teacher("Emree","Y",40)
t1.intro()
# class test():
#     pass


# class baseclass():
#      def show(self):
#           return "hello"
     

# def add_attribute(self):
#     self.b=10
 

# test=type("test",(baseclass,),{"a":5,"add_attribute":add_attribute})
# t=test()

# sonuc=test()
# sonuc=test
# sonuc=type(test)
# # sonuc=type(2)
# # sonuc=type(int)
# # sonuc=type("2")
# # sonuc=type(str)

# sonuc = t.show()
# sonuc=t.a
# t.add_attribute()
# sonuc=t.b
# print(sonuc)









class  meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        
        a={}
        
        for name,val in attrs.items():
            if name.startswith("_"):
                a[name]=val
            else:
                a[name.upper()]=val


        return type(class_name,bases,a)
    

class person(metaclass=meta):
    x=5
    y=10
    _age=40

    def hello(self):
        print("hello")


p=person()

sonuc=p.X
sonuc=p.Y
sonuc=p._age

print(sonuc)
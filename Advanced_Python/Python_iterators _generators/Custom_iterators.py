class myNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start<= self.stop:
            x=self.start
            self.start +=1
            return x 
        else:
            raise StopIteration
        


iterator=iter(myNumbers(20,30))

while True :
    try: 
        sayi=next(iterator)
        print(sayi)
    except StopIteration:
        break



# print(iterator)
# print(next(iterator))
# print(next(iterator))

# iterator =iter(myNumbers(20,30))

# for i in myNumbers(20,30):
#     print(i)
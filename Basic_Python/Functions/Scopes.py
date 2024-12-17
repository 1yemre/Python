#local
#Global

x="Global"
def my_func():
    x="local"
    print(x)

# my_func()
# print(x)

x="Global"
def my_func():
    global x
    x="local"
    print(x)

#my_func()
# print(x)


name="Ahmet" #3
def greeting():
    #name="Emre"#2
  
    def hello():
      #name="Ada"  #1
      print("Hello" , name)


    hello()

greeting()


# x=50

# def test(x):
#     print(f"x:{x}")

#     x=100
#     print(f"Changed X to {x}")

# test(x)
# print(x)


y=50

def test():
    global y
    print(f"x:{y}")

    y=100
    print(f"Changed X to {y}")

test()
print(y)
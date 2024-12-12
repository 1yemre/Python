# elemanlar değiştirlemez!!

my_list=[1,2,3]
my_tuple=(1,2,3)  # veya 1,2,3

print(type(my_list))
print(type(my_tuple))



my_list[0]=555
#my_tuple[2]=10 # give error

result=my_list[0]
result2=my_tuple[0]

# uses to method count and index  from tuple 

my_tuple2=tuple([2,3,4])


print(result)
print(result2)

print(type(my_tuple2))
# List:collection different data elements enclosed into []
# it is sequence,index follows,ordered and it is Mutable means it can do CRUD

# create list
list1=[]
print(list1,type(list1)) # [] <class 'list'>
list2=[100]
print(list2,type(list2)) #[100] <class 'list'>
list3=["hello",100,True,100j,None,(100,200)]
print(list3,type(list3))  # ['hello', 100, True, 100j, None, (100, 200)] <class 'list'>

# Index
print(list3[0])  #hello
print(list3[-1]) #(100, 200)

# Mutable
list3[-1]=55555
print(list3)  # ['hello', 100, True, 100j, None, 55555]
fruits=["apple","grapes","banana","kiwi","watermelon"]
print(fruits)
fruits.reverse()
print(fruits) #['watermelon', 'kiwi', 'banana', 'grapes', 'apple']
fruits.sort() 
print(fruits) #['apple', 'banana', 'grapes', 'kiwi', 'watermelon']

price=[200,300,100,500]
fruits.extend(price)
print(fruits)  # ['apple', 'banana', 'grapes', 'kiwi', 'watermelon', 200, 300, 100, 500]
print(fruits.count("apple"))
x=[1,2,3]
print(x)
x=fruits.copy()
print(x)  
x.clear()
print(x)  # []

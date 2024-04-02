#Nested dictionary example

book= {1:{"name":"python","isbn":2712,"department":"cse"},
       2:{"name":"DBMS","isbn":4120,"department":"Cse"},
       3:{"name":"Embedded system","isbn":7120,"department":"ECE"}}
print(book[1])
print(book[2])
print(book[3]['isbn'])

#Example of built in functions of Set function

cars1 ={"bmw","suzuki","tata","audi"}
cars2 = cars1.copy()
cars1.add("porsche") #difference add
print(cars1)
cars1.difference_update(cars2) #difference update
print(cars1)
cars2.discard("suzuki")
print(cars2) #discard function
cars1.add("bmw")
print(cars1.intersection(cars2)) #intersection
all_cars ={"bmw","suzuki","tata","audi","porsche","nissan"}
print(all_cars.issubset(cars2)) #issubset function
print(cars2.issubset(all_cars))
all_cars.pop() #pop function
print(all_cars)
print(all_cars.symmetric_difference(cars1)) #symmetric difference function
print(cars1.union(cars2)) #union function

#If elif and else condition example:

var1 = int(input("enter the value 1:")) #odd or even (if else)
if(var1%2==0):
    print("the given number",var1,"is even number")
else:
    print("the given number",var1,"is odd number")

var2 = int(input("Enter the value 2:")) #greatest of three numbers ( if elif )
var3 = int(input("Enter the value 3:"))
if(var1>var2 and var1>var3):
    print("value 1 is greater")
elif(var2>var3):
    print("value 2 is greater")
else:
    print("value 3 is greater")

#for loop example
for i in range(0,20):
    if(i%2==0):
        print("even numbers:",i)

#enumerate function

l1 = ["eat","sleep","repeat"]
for element in enumerate(l1):
    print(element)

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(5):
    if i==3:
        continue
    print(i)







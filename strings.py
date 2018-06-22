print("hello world")
greeting="hello"
name=input("pleasae enter your name :")
print(greeting + " "+ name)
split="this string \n \t is splited"
print(split)
print("hi "*5)
number="1, 2, 3, 4, 5, 6"
print(number[0::2])
today="monday"
print("hello" in  today)
print("mon" in today)

age=18
print("my age " +str(age)+ "years")
print("my age is {0} years".format(age))
print("there are {0} daysin {1},{2},{3}".format(31,"jan","feb","mar"))
print("my age is %d"%age)
print("my age is %d %s %s"%(age,"years","old"))
for i in range(1,12):
        print("the sqr of %2d is %4d and cube is %4d" %(i,i**2,i**3))
for i in range(1,12):
        print("the sqr of {0:2} is {1:<4} and cube is {2:4}" .format(i,i**2,i**3))

print(" the pi value is %12.50f"%(22/7))
print(" the pi value is {0:12.50f}".format(22/7))
#{x:y} the value y for spacing between values,x for the index of the format
for i in range(1,12):
    print("no {:2} squared is {:3} and cubed is {:5}".format(i,i**2,i**4))

name=input("whats your name ?  ")
age=int(input("whats your age {}  ".format(name)))
print("hello "+name+" you are "+str(age)+" years old")
if(age>=18):
    {
        print("and you are eligible for vote")

    }
else:
    print("and you are eligible for vote")
    print("come back in %d years" %(18-age))
    print("thank you")


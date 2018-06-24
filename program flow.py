# #{x:y} the value y for spacing between values,x for the index of the format
#
# # #for loop
#
# # for i in range(x,y,z)
# #     x is initial value
# #     y is end value
# #     z is increment
#
for i in range (1,11):
    for j in range(1,11):
        print("{0} * {1} = {2}".format(i,j,i*j),end="\t")
    print("_______________________________________________")

shop={"egg","rice","fruits","sweets"}
for i in shop:
    if i == "fruits":
       print("buying fruit")
       continue
    print("buy "+i)
#
#
for i in range(1,12):
    print("no {:2} squared is {:3} and cubed is {:5}".format(i,i**2,i**4))
number="9,56,989,651,458,874"
for i in range(0,len(number)):
    #to eliminate coma
    if number[i] in "123456789":
        print(number[i],end="")

for char in number:
    if char in "0123456789":
        print(char,end="")

for state in {"cute","smart","handsome"}:
    print("kutty selva is "+state)
    print("this is {}".format(state))
# if case
name=input("whats your name ?  ")
age=int(input("whats your age {}  ".format(name)))
print("hello "+name+" you are "+str(age)+" years old")
if(age>=18):

        print("and you are eligible for vote")


else:
    print("and you are eligible for vote")
    print("come back in %d years" %(18-age))
    print("thank you")

#elif

guess=int(input("guess a number between 1 to 10"))
if guess<5:
    print("guess higher")
    guess=int(input())
    if guess==5:
        print("you passed this test")
    else:
        print("sorry try again ")
elif guess>5:
    print("please guess lower")
    guess = int(input())
    if guess==5:
        print("you guessed correctly")
    else:
        print("sorry try again ")
else:
    print("guessed in first attempt")

#common examples

ag=int(input("whats your age ? "))
if 16<= ag <65:
    print("have a good day")


#challenge 1

ip=input("enter your ip address")
ip+="."
seg=1
leng=0
for i in ip:
    if i ==".":
        print("segment {} contains {} chars".format(seg,leng))
        leng=0;
        seg+=1;
    else:
        leng+=1


  #while loop
city = ["madurai", "chennai", "coimb", "trichy"]
chk = ""
while chk not in city:
    chk=input("enter a city : ")
    if chk == "quit":
        print("exits")
        break
print("out of here")

#challenge 2
import random
high=10
ans=random.randint(1,high)
print("guess a number between 1 to 10")
guess=0
while guess != ans :
    guess=int(input())
    if guess==0:
        break
    if guess<ans:
        print("guess high")
    elif guess>ans:
        print("guess low")
    else:
        print("correct")
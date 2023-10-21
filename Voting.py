#simple voting eligibility identifier program example
print("welcome, please enter your name")
name = str(input("NAME:-"))
print("hello",name)
age = int(input("enter your age:-"))
if age>18:
    print("you are eligible to vote")
elif age==18:
    print("you are eligible to vote")
else:
    print("unfortunately, you are not eligible to vote")

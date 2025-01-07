# functions are a ways to wrap your code
# into reusable units

# How you define a function
# You only define the function ONCE!!!!!!
# Whatever I pass inside the parenthesis is called a parameter
# A paramater is a placeholder for future information 
def sayHello(name,age, adress):
    print(f"say hello {name}")
    print(f"Hello Governor, your adress is {adress}")
    print(f"welcome back {name}")
    print(f"your age is {age}")


# Once you define a function
# You must call or invoke the function
# When I pass in information into the call function its called an argument 
# sayHello("Fabio", 16, "125 north lawndale")
# sayHello("Devin", 25, "345 north lawndale")
# sayHello("Lara", 45, "565 north lawndale")

def determinEligibility(age):
    # If your age is over 18, you can vote,
    # Otherwise you can't
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote yet")

# determinEligibility(12)
# determinEligibility(15)
# determinEligibility(19)


def willYouGraduate(gpa, credits, SAT):
    # gpa :Number float variable
    # credits: Number variable
    # SAT: Boolean value
    if (gpa == 3.0) and (credits>=28) and (SAT == True):
        print("You passed. Good luck in College")
    elif (gpa <3.0) or (credits < 28) or (SAT != True):
        print("Back to the drawing board")
    else:
        print("Talk to your counselor")

# willYouGraduate(2.8, 15, True)
# willYouGraduate(3.4, 30, True)
# willYouGraduate(4.0, 28, True)

# Return Statement


def add(x,y):
    z = x + y
    return z


def subtract(x,y):
    z = x - y
    return z


def multiply(x,y):
    z = x * y
    return z


def divide(x,y):
    z = x / y
    return z


# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last 
full_name = create_name("Spongebob", "Squarepants")
print(full_name)
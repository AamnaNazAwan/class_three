def greet():
    print("hello world!")

greet()


#function with parameter
def greet(name):
    print(f'hello{name}')

greet("alice")

#adding two numbers
def add(a,b):
    return a+b
result = add(2,3)
print(result)


def greet(first_name,last_name):
    print(f"hello{first_name} {last_name}")

greet(first_name= "john", last_name="alice")
greet(last_name="alice",first_name="john")

def add(*args):
    return sum(args)

result = add(1,2,3,4)
print(result)

#def greet(**kwargs):


#ENCLOSING VARIABLES

def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20
        print (x)

    inner_function()
    print(x)

outer_function()

# GLOBAL VARIABLE
x = 10
def my_function():
    print(x)

my_function()
x  = 9
print(x)

#LOCAL VARIABLES
def my_function():
     x= 10
     print(x)
my_function()

#FUNCTION FOR CALCULATING RADIUS
def calculate_area(radius):
    pi = 3.142
    return pi* (radius ** 2)

def describe_circle(radius,area):
    print(f"A circle with radius{radius} has an area of {area: .2f}")

radius = 5
area = calculate_area(radius)
describe_circle(radius,area)

#adding two numbers and then subtract number from this addition value
'''def addition(a,b):
    return a+b

def subtration(addition,sub):
    return addition-sub
    print(f"the value is {subtraction}")

results = addition(2,3)
subtration(results,20)'''


                   #LAMBDA FUNCTION
add_lambda = lambda a,b:a+b


#common uses of lambda
#map()
numbers = [1,2,3,4,5]
squares = map(lambda x:x**2,numbers)
print(list(squares))

#sorted()
points = [(1,2),(3,1),(0,-1)]
points_sorted = sorted(points,key=lambda point: point[1])
print(points_sorted)

#filter()
numbers = [1,2,3,4,5]
evens = filter(lambda x:x%2 == 0,numbers)
print(list(evens))

def make_multiplier(n):
    return lambda x:x*n

doubler = make_multiplier(2)
tripler = make_multiplier(3)

print(doubler(5))
print(tripler(5))



1. 

num = 5

def my_func():
    print(num)

my_func()

# it will print 5. 
# num is a global variable and my_func
# is calling on it 

2. 

num = 5

def my_func():
    num = 10

my_func()
print(num)

# still prints 5 
# num global is 5, while num local in my_func is 10. 

3. 

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# prints out 10
# global num is localized to the function and reassigned. 


4. 

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# prints hello world
# outer_ver is in scope

5. 

def my_func():
    num = 10

my_func()
print(num)

# error 
# num is not defined globally

6. 

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# inner 1 25
# inner 2 15
# inner_func1 uses the x defined in the function 
# inner_func2 uses the x defined out of scope, since its not defined
# in inner_func2
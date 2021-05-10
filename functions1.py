def greeting():
    print("Hello World")

# greeting()

    # HEY! PYTHON!!! I wronte a function
    # It's called "greeting", go find it and run it
    # Please, and thank you!

# Not a real example but think of it like this
    # def squareNumbers(var firstNumber, var secondNumber):
    #     return [VALUE ASSIGNED TO firstNumber] * [VALUE ASSIGNED TO secondNumber]

def square(num):
    return num * num

# print(square(2))

global_variable_example = "Foo"

def localscopefunction():
    local_variable_example = "Bar"
    print(global_variable_example + " is Global")
    print(local_variable_example + " is Local")

# print(localscopefunction + " Is this real???")

def secondlocalscopefunction():
    local_variable_example = "Baz"
    print(local_variable_example + " is Local")

localscopefunction()
secondlocalscopefunction()
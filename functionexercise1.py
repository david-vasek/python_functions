# Example 1: Madlib function
# def madlib1(name, subject):
#     return ("This is %s, his favorite subject is %s" % (name, subject))


# def ask_for_user_info():
#     user_name = input("What is your name?")
#     user_subject = input("What is your subject?")

#     print(madlib1(user_name, user_subject))

# ask_for_user_info()

# Celsius to Fahrenheit conversion
# def temp_converterC(celciustemp):
#     inFahrenheit = (celciustemp * 9/5) + 32
#     return("If it is %s degrees in celcius, it is %s degrees fahrenheit. " % (celciustemp, inFahrenheit))

# print(temp_converterC(user_temp))

# Fahrenheit to Celcius
def temp_converterC(fahrenheitTemp):
    inCelcius = (fahrenheitTemp- 32) * 5/9
    return("If it is %s degrees in fahrenheit, it is %s degrees in celcius." % (fahrenheitTemp, inCelcius))

print(temp_converterC(70))



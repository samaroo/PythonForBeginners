# Notes
#
# Functoins
#
# use keyword "def" to define functions
#   "def functionName():"
# "functionName()" to call function
# you can define fuctnions with parameters but they dont have to be any datatype
# "def functionName(temp)"
# adding another parameter with an asteriks before it in the function definition will allow you to pass in extra parameters
#   "def functionName(one, two, three, *extra)"
#       now you can pass in as many more parameters as you'd like
#       extra parameters are stored in the "extra" variable as a tuple
# when returning data, you dont have to specify what you're returning
#
# Modules
#
# They are like mini libraries that you can import in other .py files
# Modules contain a list of functions that can be used in other files
# To import a module, use "import filename"
# file mest be in the same directory as the .py file you are trying to import to
# "import randomModule
#   randomModule.randomFunctionInModule()"

# farenheight to celcius calculator

def fToC(f):
    return (f - 32) / 1.8

# celcius to farenheight calculator

def cToF(c):
    return c * 1.8 + 32

# calculator that converts both ways, second parameter is bool, if true, parameter is celsius

def converter(x, y):
    return (x * 1.8 + 32 if y else (x - 32) / 1.8)

# test

print(fToC(32))
print(fToC(212))

print(cToF(0))
print(cToF(100))

print(converter(32, False))
print(converter(212, False))
print(converter(0, True))
print(converter(100, True))

"""My first exercise in COMP110!"""
__author__ = "730564205"


# function signature tells us what the function expects to take input or output
# we are self creating a keyword "greet" (identifier) using def keyword
# if you just type greet, its just referring its name, not actual calling
def greet(name: str) -> str:  
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


# argument with an = is called an keyword argument
# just clearer way on what happens implicity
# arguments can be an expression!
# expression is made of one or more operands: 
# Ex: operand is a single value. 2 is an expression. 
# (expression with no operators are called literal values)
# expression can be seperated by operators
#  2 * 3 is an expression. 
# greet() is a operand bc functions returns a value
# an expression returns(produces) a single typed value: ex: primitive type or object 
# in expression, its allowed to use +, - ,/ ,= (operator) to combine/assign operands

greet(name="Sam" + "antha")
# Insidethe argument () , its an expression: overall a value
# inside argument "Sam" + "antha" -> "Samantha"  
# expression dont have to be operators, just a single value
# but it can made of/seperated by one or more operators


greet(greet("Annie"))
# The entire Function call is an expression too! not just argument
# so function call it returns a single typed value
# in this case,  greet("Annie") means -> "Hello, Annie"
# "Hello, Annie" is one single value expresssion
# returns "Hello, Annie!" inside outer greet()
# becomes:  greet("Hello, Annie")

# conculsion: value(value)  
# inside paranethsis is a value and then whole thing later becomes a single value
# you can seperate a primitve type expressions by an operand.
# you cant use operands with objects
# evaluate an expression means return a expression into a single typed value
# expression : you can cross out the orignial line and wrote a typed value

'''
primitive types
eg: 2 means 1 + 1
    "hi!"  means "hi" + "!"
    cannot seperate True with operands
    but can use with operands True + True = 2

Objects
cannot sepreate by operands, or use with operands
'''

'''
__name__ is python file memory attribute
# in file hello.py

print(__name__)


why prints __main__ when hello.py is running?
 bc the main means the program starts to run.
 so python's memory attribute will be assigned to a value __main__ 
 when hello.y starts to run
'''
 
 
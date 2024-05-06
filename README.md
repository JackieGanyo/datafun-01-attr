# datafun-01-attr

Module 1 Data Fundamentals 

⭐Module 1: Learn Python Basics
The only way to learn Python is by using Python. Don't try to memorize. Instead, get familiar with terms, and read short introductions. We'll write our Python online, and use the interactive Skill Drills to clarify understanding. Try each Skill Drill before you start the lesson - it's a bit like a pre-test (you can take them as many times as you like and we only keep the highest score). Read the project requirements early and use it to guide your practice. You'll be able to finish both more efficiently. The projects are a great place to keep all your Python notes. The projects are for you  - see how adding Python to your skills can help you as a data analyst. 

Key Skills In This Lesson
In Module 1, we cover some fundamental programming concepts. Take the associated Skill Drill for each skill before and/or after reading the lesson. Take them as often as you like to help master the concepts. 

Explain Your Code with Comments
Use print() Function
Recognize Data Types
Perform Operations On Data
Call More Built-in Functions
Provide Function Inputs (Arguments)
Explore Function Output (Return Values)
Store Data in Named Variables
Import Code from the Standard Library
Create Useful Text with Formatted Strings
Create the Module main() Function
Create a Reusable Python Module
Optional Bonus:

1. Code Like a Pro with Type Hints

 

Instructions
Read through the notes below. As you go, type the code or copy/paste and modify the code - it's the only way to get an understanding of how picky code can be. Choose any of the online options listed at: Try Python Online.
 
Read Chapter 02 in our textbook and work through the exercises to get a more complete introduction to these critical basics.  The order in the book is a bit different, but all of Chapter 02 is important. A book is still an efficient way to learn a programming language well. Read, and remember, it is critical to type/try as you go. 

These key skills are introduced below. Work in your online interpreter as you go through the content. Save your practice (or take screenshots) to verify and earn credit for your efforts. 

1. Explain Your Code with Comments
Outcomes:

Learn the importance of documenting your code using comments.
Start with multi-line docstrings at the beginning of your script to describe its purpose and authorship.
Use single-line comments to clarify specific parts of your code.
Don't over comment. Strive for code that is clear and doesn't require extensive comments. 

Use comments to explain pieces of code and make your code more readable. Professionals typically start with a multi-line docstring that introduces their code. As you go, add single line comments as needed to explain your work.  They start and end with three quotes. 

"""
**Purpose: Practice Python**

This is a multi-line comment (or string), 
also called a docstring, 
widely used by professionals to document code files.

Note the use of three quote marks together 
to open the string
and three quote marks together
to close it. 
"""

# This is a single-line comment - it starts with a hash
a = 3 # a is assigned the value of 3
b = 4 # you can start these to the right of your code 
Practice writing both kinds of comments. Note either single or double quotes should work (as long as you are consistent). 

 

**2. Use print() Function**
Outcomes:

Get familiar with Python's print() function to display output.
Use print() as needed to display simple output
The built-in print() function is used to display information to the user.  Text-based information must be wrapped in quotes. Numbers and expressions don't need quotes - the result of the expression will be displayed. Calling print() with no arguments will print a blank line.

print ("Hello, World!")
print(52+37)
print()
 

**3. Recognize Data Types**
Outcomes:

Understand various data types in Python like strings (str), integers (int), floating-point numbers (float), complex numbers (complex), decimals (decimal), booleans (bool), lists (list), and the null value (None).
Use the type() function to identify data types.
We do not specify data types - instead Python determines the type from the value provided.
Analysts must understand data and data types. Know the difference between these types of data. The name in bold is the actual data type name in Python - it's what you get if you ask Python to tell you the type, e.g. `type("Hello!")`. The second is our common English term for that kind of data and a general description. 

str (String): Used for text and characters. Example: "Data Analysis" - helpful for handling textual data like names, labels, or categorical information.
int (Integer): Represents whole numbers without a decimal. Example: 100 - useful for counting items, indexing, or any scenario where fractional numbers are not needed.
float (Floating Point Number): Represents real numbers and can include fractions (decimals). Example: 10.5 - crucial for precise measurements or calculations requiring decimal points.
bool (Boolean): Represents two values: True or False. Example: True - crucial for decision-making logic in data processing, like filtering data.
list (List): A collection of ordered items, which can be of mixed data types. Example: [1, 2.5, 'data'] - useful for storing sequences of data, iterating over them, or performing operations on collections of values.
None: The Python null value. It's used to represent the absence of a value or a default state. In data analysis, None can be used to indicate missing or unassigned data.
Advanced: complex (Complex Number): Used for complex numbers, having a real and an imaginary part. Example: 3 + 5j - useful when working with electrical engineers.
Advanced: decimal (Decimal): Provides decimal floating-point arithmetic with more precision than float. Example: Decimal('0.10') - essential when exact decimal representation is required, such as in financial calculations.
 

type("Data Fundamentals"
type(4)
type(5.2)
type(True)
type([1,6,3,10])
type(None)
 

**4. Perform Operations on Data**
Outcomes:

Recognize and use Python's arithmetic, Boolean, and comparison operators.
Employ operators to perform calculations and logical operations in Python.
Just like Excel, Python uses symbols to perform common operations.

Arithmetic Operators

+ (Addition): Adds two operands.
- (Subtraction): Subtracts right operand from left.
* (Multiplication): Multiplies two operands.
/ (Division): Divides left operand by right.
% (Modulus): Returns remainder of division.
** (Exponentiation): Raises left operand to power of right.
// (Floor Division): Divides and returns integer part of quotient.
Boolean (Logical) Operators

and: True if both operands are true.
or: True if either of the operands is true.
not: True if operand is false.
Comparison Operators

== (Equal to): True if both operands are equal.
!= (Not equal to): True if operands are not equal.
> (Greater than): True if left operand is greater than right.
< (Less than): True if left operand is less than right.
>= (Greater than or equal to): True if left is greater than or equal to right.
<= (Less than or equal to): True if left is less than or equal to right.
print(2+5)
print(12 % 14)
print(2**8)
print(True and True)
print(not True)
print(4==2*2)
print(10 >= 5**2)
 

**5. Call More Built-in Functions**
Outcomes:

Use Python's built-in functions to perform various operations.
Understand functions may operate on single values, multiple values, or collections.
Provide inputs of the correct type to call built-in functions successfully.
You may not have to write all the calculations yourself. Python was designed for math and statistics and has many useful functions built in. When you see a name followed by parentheses (like sum()), that's a function call. We say we are calling the function or asking it to execute. Understanding what inputs a function requires and what output it returns is key. Some functions don't need any inputs, e.g., providing a prompt is optional when calling input(), while others require specific information in a specific format. Similarly, some functions return values, while others perform actions without returning anything, e.g. print(). 

Functions We Can Call Without Passing in Anything (or an optional string)

print(): Displays the output of an expression or variable. It doesn't return a value.
input(): Reads a line from input and returns it as a string. We can provide an optional string as the prompt. 
Functions Operating on a Single Value

type(): Returns the data type of an expression or variable.
abs(): Returns the absolute value of a number.
round(): Returns a number rounded to a specified number of decimal places.
string(): Returns a string from another data type. Useful for concatenating non-string types with strings.
int(): Returns an int from a string or other data type if possible. 
float(): Returns a floating point number from a str or other data type if it can.
help(): Returns a helpful description of the provided function or module name, e.g., help(abs)
Functions Operating on a Collection or Many Values

min(): Returns the smallest value in an iterable or the smallest of several arguments.
max(): Returns the largest value in an iterable or the largest of several arguments.
sum(): Returns the total of all items in an iterable.
len(): Returns the number of items in an object. NOTE: This must be a single object, not multiple values. 
Function that Returns a Range of Values

range(): Returns a sequence of numbers, useful in loops. The range it returns is NOT a list. But to process the items as a list, you can cast it to a list with the list() function. 
Functions That Return a List

sorted(): Returns a sorted list from the given iterable.
list(): Converts other data types into a list and returns it.
Practice calling these built-in functions. Try the following in your online interpreter. When these examples work, try some new variations. It's a great thing when you introduce small errors and have to try to figure out how to fix them. 

# examples of calling built-in functions
abs(-40.8)
min(3, 1, 4, 1, 5, 9)
max(3, 1, 4, 1, 5, 9)
len([44,21,34])  # requires a single argument such as a list or string
sum(1, 2, 3, 4, 5)
sorted([9,8,8,2,4,5,5,1])
help(list)

# wrap each expression in print() to display the result
print(  min(3,1,4)  )
6. Provide Function Inputs (Arguments)
Outcomes:

Provide appropriate inputs to functions by passing in appropriate arguments.
Understand and employ different argument types.
Employ optional arguments as needed.
round(18.1234567)    # try with no argument
round(18.1234567, 2  # specify the decimal places
print("Starting up....)
print()  # omit the optional argument
input("Please enter your name:")
input() # input without a prompt can be confusing
 

**7. Explore Function Outputs (Return Values)**
Outcomes:

Understand what it means to call a function (also referred to as executing or invoking the function).
Understand that we can refer to a function without calling it by omitting the parentheses.
len("hello")                # call the function len()
type(len("hello"))          # what type is returned when calling len()?
print( type(len("hello")) ) # call print() on the result of the type() function call

help(len)   # Sometimes, we just pass a function - but we don't want to call it
help(len()) # Oops: What happens if we pass - and call - the function?

**8. Store Data in Named Variables**
Outcomes:

Use variables to store and manipulate data.
Understand Python's dynamic typing.
Follow variable naming conventions.
We can store values in named variables and use those variables in reusable calculations. For example, I might use a variable named pet_weight_lbs to hold the pet weight is in pounds so I can reuse processing logic to find  overweight pets. 

pet_weight_lbs = 10.5    # a float variable
hasCreditCardOnFile = True  # True and False are capitalized
The = (equal sign) in Python is an assignment operator. We are creating a variable name (pet_weight_lbs), and using it to temporarily hold the value 10.5. Python will figure out what type pet_weight_lbs is by the value we provide. Python recognizes it and automagically makes it a float. We can say type(pet_weight_lbs) and it will return 'float'. 

**Follow Variable Naming Conventions**
Name your variables using whole words with underscores between them. This is the traditional Python way. Communicate clearly and always include the units information in variable names. Some of the most expensive errors have been caused by mistaking the units for a given variable. You can't leave spaces, you can't start with a number, and there's a few more rules, but if you follow most examples, you should be good. 

# We don't specify types - we just provide the data

name = "Instructor"
course_count = 6
is_experienced = True
hours_invested = 2.5

# Python determines the type from the value provided

type(name)
type(course_count)
type(is_experienced)
type(hours_invested)

Variables can hold individual values or more complex things. To create a Python list, just put your values in square brackets and separate them with commas. Now you can call the built-in function sum() on whatever your numbers list holds.  We pass in the variable by putting it inside the parentheses of the function sum(). The function returns the sum of the items in the list - either an int or a double or something else, depending on what values were in the list. 

Try defining several lists. Which built-in functions need lists and which can just handle multiple values. Use the online interpreter. Lists don't have to hold values that are all the same type - what impact does that have? Explore. 

# define some example lists
months = list(range(1,13))
numbers = [7, 6, 5, 8, 8, 4, 5, 7, 8, 6]
Optional: Add Type Hints
In Python, we don't specify the type - the Python interpreter determines it from the data we provide. This is called "dynamic typing". It makes it really easy to get started, but it can delay errors until our program is actually running. What does it mean to take the square root of "Hello" or -567.8? Being clear about our intentions helps communication. Since Python 3.5, we can add type hints - they look a lot like static types in other languages and are frequently used in industry to improve communication about what our code is supposed to do. 

They are optional - but they are quite easy to add and are  highly recommended if you want your code to look professional and up to date.  Type hints have no effect on the Python interpreter, but there are outside programs (e.g., Pyright, Mypy, Pylance) that can read them and help us help find errors. 

name:str = "Instructor"
course_count:int = 6
is_experienced:bool = True
hours_invested:float = 2.5
numbers:list = [7, 6, 5, 8, 8, 4, 5, 7, 8, 6]
Side benefit: You'll be more ready to take advantage of the new Mojo language 🔥- syntax like Python, but thousands of times faster. Be one of the first to check it out! 

**9. Import Code from the Standard Library**
Outcomes:

Make use of the many Python Standard Library modules.
Python comes with a broad and powerful Python Standard Library that adds additional features. There's a module for math and a module for statistics. To use them just include an import statement at the top of our Python code. To import the math module, say "import math", to import the statistics module, say "import statistics". 

# First, import modules at the top (after the docstring introduction)

import math
import statistics

# Now, we can use their functions.

# Square root
print(math.sqrt(16))

# Trigonometric functions (e.g., sine, cosine)
print(math.sin(math.pi / 2))
print(math.cos(0))

Learning the standard library takes time and experience. Python syntax can be mastered in days or weeks, but it can take months (and years) to make good use of all the free code to make projects better, faster, and more enjoyable.

If you have programming experience, spend some time this module checking out more modules from the standard library, like datetime, pathlib, csv, json, and sqlite3. 

Be More Specific
When we only require a specific function or class from a module, we can choose to import just that particular element. This is more efficient as it only loads the required component into memory. For example, if we need only the pi constant from the math module, we can import it directly using from math import pi. Similarly, to import the Path class from the pathlib module, we use from pathlib import Path. And if we need the datetime class from the datetime module, we write from datetime import datetime. Selective importing can help make code more efficient and more readable.

from math import pi
from pathlib import Path
from datetime import datetime # from datetime module, import just the datetime object
10. Create Useful Text with Formatted Strings
Outcomes:

Use f-strings to provide useful information combining text and expressions. 
You might have noticed that calling print(result) doesn't always provide useful output. We have to explain what the result represents. To print useful information, use formatted strings (f-strings). Formatted strings combine text and expressions so output has meaning. Professionals use f-strings everywhere.  

To use f-strings: Add quotes around the text and put an f directly in front of the opening quote. Use triple quotes (for multi-line strings) or quotes for a single line. Inside the string, wrap expressions in curly braces. 

course_count = 6
course_count_string = f"I have taken {course_count} course(s) towards my degree."
The easiest way to provide meaning is just to add an equals (=) after each expression (inside the curly braces).

is_experienced = True
is_experienced_string = f"{is_experienced=}"
Python IDEs and f-strings: You may be able to select a variable name (double-click) and hit the curly brace key to wrap it in curly braces. Similarly by selecting content to wrap in quotes. Sometimes, trying to be helpful, if you type a quote, it may give you two - one to open your text and one to close.  It's trying to be helpful. Be patient and try different things. Code is special. 

**11. Define the Module main() Function**
Outcomes: 

Understand the use of a module main() function. 
Create a useful main() for a custom module.
In Python, a module is a file (also called a script) containing Python code. It may define functions, classes, or variables. Modules help us organize our code and make it easy to reuse common utility functions in our projects.

In Python (as in other languages), professional code typically includes a main() function that encapsulates the primary functionality of the script. The main() function serves as the entry point for a program - that is, the first line of code that runs when a script is executed.

To define the main() function for our module, we:

Start with the def keyword. 
Name the function.
Add parentheses immediately after the name.
Follow the parenthesis with a (:).
Indent each statement in the function.
Keep the spacing / indentation consistent - in Python a tab is not equal to 2 spaces - or 4 spaces. Tabs and spaces are different. These things we don't see are typically called whitespace - and in Python, whitespace matters a great deal! 

def main():  # note use of def keyword and the colon (:)
  ''' The main code to execute when running this module/script/file'''
  print(course_count_string)  # indent each statement with 2 spaces
  print(is_experienced_string)
  print(hours_invested_string)
  print(numbers_string)
  print(radius_area_string)
  print(my_stats_string)
 

**12. Create a Reusable Python Module**
The goal is this course is to learn to write reusable, well-formatted and documented code that can be used to reliably get valuable information from data. Planning and organizing your project is an important part of every project.  

Code Organization
Python code is organized. Anything that resolves to a value is an expression (e.g. a==b), and a single executable statement is the smallest part of a Python script (program). Python is written in a file / script / module just as they did for the math module, the statistics module, and the datetime module from the standard library. If the file name is math.py, the module name is math. A package is a directory hierarchy with several modules. A library (e.g., the Python Standard Library) is a collection of modules and packages. 

Running Code
The Python interpreter runs the code. As it does, it manages information about your project. The Python interpreter has its own variables as it works. To keep them from getting confused with ours, the Python interpreter names its variables with dunders (double underscores before and after). That way, the interpreters __name__ variable doesn't get confused with any variable we might call "name" (pretty common, actually).  When you see dunders, you know that information is managed by the Python interpreter. 

Reminders
When writing Python, there's a few things to remember. 

In Python, spelling matters - it must be exact. 
In Python, capitalization matters - my_temp_f is not the same as My_Temp_F. 
In Python, spacing matters - tabs are not the same as spaces and spacing has meaning. Spacing is very important. 
Include the measuring units in the name of all numeric variables. 
Make your code look like others. Professionals uses tools to format code into standard appearance and conventions. Start now. 
Be valuable by making your team better and more functional  - be creative in your work and your problem-solving, but clear and conventional in your code. 
One Last Thing
Add the following at the end of your script.

if __name__ == "__main__":
    main()
This ensures that main() is called only when the script is executed directly, not when it's imported as a module in another script. It's a common best practice in Python. You don't have to memorize it and you don't have to type it from scratch. Just go to any professional Python script and you'll likely find it at the bottom. You can copy and paste it. Try it. The purpose will be more clear when we use our new code again in Module 2. 

Explanation (Optional)

When we run a Python script, the Python interpreter sets a  __name__ variable for each module in our running program. 

If the module is imported, its __name__ is set to the module name (e.g. "math", or "statistics").
If the module is the one that was actually run/called/executed, it is said to be the main module and the interpreter sets that module's __name__ variable to "__main__" (a special interpreter string value that indicates this is the main module that was executed). Only module gets to be "__main__".  In short, only if our script is the one being executed, then run our main() function. 
 

Some Online Experiments in Python
"""
Practicing with code comments and the built-in print function.
Dr. Case
Jan 2024
"""
print("Playing with Python")

# Single-line comment - starts with a hash
x = 22 # assigning a value to a variable
y = 77 # assigning a value to another variable

# calling built-in print() function with one argument is easy
print(x)
print(y)

print("That's nice, but not very helpful. Which is which?")
print()

# call print() with many arguments - just separate them by commas
print("x is equal to ", x, " and y is equal to ", y)
print("That's better, but a lot of work. Anything better?")
print()
# printing with an f-string or formatted string
# (like the cool kids do)
# just add an f just before the opening quote
# now you can insert Python expressions wherever you like
# Just wrap them in curly braces.
print(f"x is {x} and y is {y}.")
print()
print("Nice! Anything else I should try?\n") # \n adds a new line
# To be SUPER cool, try this bit of syntactic sugar
# At the end, just INSIDE a set of curly braces, add =
# It will AUTOMAGICALLY pretty print the name and value!
print(f"{x=}, {y=}")
print("Dang. That's fun! All done playing for now!")
image.png

⭐Module 1: Learn Python Basics
The only way to learn Python is by using Python. Don't try to memorize. Instead, get familiar with terms, and read short introductions. We'll write our Python online, and use the interactive Skill Drills to clarify understanding. Try each Skill Drill before you start the lesson - it's a bit like a pre-test (you can take them as many times as you like and we only keep the highest score). Read the project requirements early and use it to guide your practice. You'll be able to finish both more efficiently. The projects are a great place to keep all your Python notes. The projects are for you  - see how adding Python to your skills can help you as a data analyst. 

Key Skills In This Lesson
In Module 1, we cover some fundamental programming concepts. Take the associated Skill Drill for each skill before and/or after reading the lesson. Take them as often as you like to help master the concepts. 

Explain Your Code with Comments
Use print() Function
Recognize Data Types
Perform Operations On Data
Call More Built-in Functions
Provide Function Inputs (Arguments)
Explore Function Output (Return Values)
Store Data in Named Variables
Import Code from the Standard Library
Create Useful Text with Formatted Strings
Create the Module main() Function
Create a Reusable Python Module
Optional Bonus:

1. Code Like a Pro with Type Hints

 

Instructions
Read through the notes below. As you go, type the code or copy/paste and modify the code - it's the only way to get an understanding of how picky code can be. Chose any of the online options listed at: Try Python Online.

Read Chapter 02 in our textbook and work through the exercises to get a more complete introduction to these critical basics.  The order in the book is a bit different, but all of Chapter 02 is important. A book is still an efficient way to learn a programming language well. Read, and remember, it is critical to type/try as you go. 

These key skills are introduced below. Work in your online interpreter as you go through the content. Save your practice (or take screenshots) to verify and earn credit for your efforts. 

1. Explain Your Code with Comments
Outcomes:

Learn the importance of documenting your code using comments.
Start with multi-line docstrings at the beginning of your script to describe its purpose and authorship.
Use single-line comments to clarify specific parts of your code.
Don't over comment. Strive for code that is clear and doesn't require extensive comments. 

Use comments to explain pieces of code and make your code more readable. Professionals typically start with a multi-line docstring that introduces their code. As you go, add single line comments as needed to explain your work.  They start and end with three quotes. 

"""
Purpose: Practice Python

This is a multi-line comment (or string), 
also called a docstring, 
widely used by professionals to document code files.

Note the use of three quote marks together 
to open the string
and three quote marks together
to close it. 
"""

# This is a single-line comment - it starts with a hash
a = 3 # a is assigned the value of 3
b = 4 # you can start these to the right of your code 
Practice writing both kinds of comments. Note either single or double quotes should work (as long as you are consistent). 

 

2. Use print() Function
Outcomes:

Get familiar with Python's print() function to display output.
Use print() as needed to display simple output
The built-in print() function is used to display information to the user.  Text-based information must be wrapped in quotes. Numbers and expressions don't need quotes - the result of the expression will be displayed. Calling print() with no arguments will print a blank line.

print ("Hello, World!")
print(52+37)
print()
 

3. Recognize Data Types
Outcomes:

Understand various data types in Python like strings (str), integers (int), floating-point numbers (float), complex numbers (complex), decimals (decimal), booleans (bool), lists (list), and the null value (None).
Use the type() function to identify data types.
We do not specify data types - instead Python determines the type from the value provided.
Analysts must understand data and data types. Know the difference between these types of data. The name in bold is the actual data type name in Python - it's what you get if you ask Python to tell you the type, e.g. `type("Hello!")`. The second is our common English term for that kind of data and a general description. 

str (String): Used for text and characters. Example: "Data Analysis" - helpful for handling textual data like names, labels, or categorical information.
int (Integer): Represents whole numbers without a decimal. Example: 100 - useful for counting items, indexing, or any scenario where fractional numbers are not needed.
float (Floating Point Number): Represents real numbers and can include fractions (decimals). Example: 10.5 - crucial for precise measurements or calculations requiring decimal points.
bool (Boolean): Represents two values: True or False. Example: True - crucial for decision-making logic in data processing, like filtering data.
list (List): A collection of ordered items, which can be of mixed data types. Example: [1, 2.5, 'data'] - useful for storing sequences of data, iterating over them, or performing operations on collections of values.
None: The Python null value. It's used to represent the absence of a value or a default state. In data analysis, None can be used to indicate missing or unassigned data.
Advanced: complex (Complex Number): Used for complex numbers, having a real and an imaginary part. Example: 3 + 5j - useful when working with electrical engineers.
Advanced: decimal (Decimal): Provides decimal floating-point arithmetic with more precision than float. Example: Decimal('0.10') - essential when exact decimal representation is required, such as in financial calculations.
 

type("Data Fundamentals"
type(4)
type(5.2)
type(True)
type([1,6,3,10])
type(None)
 

4. Perform Operations on Data
Outcomes:

Recognize and use Python's arithmetic, Boolean, and comparison operators.
Employ operators to perform calculations and logical operations in Python.
Just like Excel, Python uses symbols to perform common operations.

Arithmetic Operators

+ (Addition): Adds two operands.
- (Subtraction): Subtracts right operand from left.
* (Multiplication): Multiplies two operands.
/ (Division): Divides left operand by right.
% (Modulus): Returns remainder of division.
** (Exponentiation): Raises left operand to power of right.
// (Floor Division): Divides and returns integer part of quotient.
Boolean (Logical) Operators

and: True if both operands are true.
or: True if either of the operands is true.
not: True if operand is false.
Comparison Operators

== (Equal to): True if both operands are equal.
!= (Not equal to): True if operands are not equal.
> (Greater than): True if left operand is greater than right.
< (Less than): True if left operand is less than right.
>= (Greater than or equal to): True if left is greater than or equal to right.
<= (Less than or equal to): True if left is less than or equal to right.
print(2+5)
print(12 % 14)
print(2**8)
print(True and True)
print(not True)
print(4==2*2)
print(10 >= 5**2)
 

5. Call More Built-in Functions
Outcomes:

Use Python's built-in functions to perform various operations.
Understand functions may operate on single values, multiple values, or collections.
Provide inputs of the correct type to call built-in functions successfully.
You may not have to write all the calculations yourself. Python was designed for math and statistics and has many useful functions built in. When you see a name followed by parentheses (like sum()), that's a function call. We say we are calling the function or asking it to execute. Understanding what inputs a function requires and what output it returns is key. Some functions don't need any inputs, e.g., providing a prompt is optional when calling input(), while others require specific information in a specific format. Similarly, some functions return values, while others perform actions without returning anything, e.g. print(). 

Functions We Can Call Without Passing in Anything (or an optional string)

print(): Displays the output of an expression or variable. It doesn't return a value.
input(): Reads a line from input and returns it as a string. We can provide an optional string as the prompt. 
Functions Operating on a Single Value

type(): Returns the data type of an expression or variable.
abs(): Returns the absolute value of a number.
round(): Returns a number rounded to a specified number of decimal places.
string(): Returns a string from another data type. Useful for concatenating non-string types with strings.
int(): Returns an int from a string or other data type if possible. 
float(): Returns a floating point number from a str or other data type if it can.
help(): Returns a helpful description of the provided function or module name, e.g., help(abs)
Functions Operating on a Collection or Many Values

min(): Returns the smallest value in an iterable or the smallest of several arguments.
max(): Returns the largest value in an iterable or the largest of several arguments.
sum(): Returns the total of all items in an iterable.
len(): Returns the number of items in an object. NOTE: This must be a single object, not multiple values. 
Function that Returns a Range of Values

range(): Returns a sequence of numbers, useful in loops. The range it returns is NOT a list. But to process the items as a list, you can cast it to a list with the list() function. 
Functions That Return a List

sorted(): Returns a sorted list from the given iterable.
list(): Converts other data types into a list and returns it.
Practice calling these built-in functions. Try the following in your online interpreter. When these examples work, try some new variations. It's a great thing when you introduce small errors and have to try to figure out how to fix them. 

# examples of calling built-in functions
abs(-40.8)
min(3, 1, 4, 1, 5, 9)
max(3, 1, 4, 1, 5, 9)
len([44,21,34])  # requires a single argument such as a list or string
sum(1, 2, 3, 4, 5)
sorted([9,8,8,2,4,5,5,1])
help(list)

# wrap each expression in print() to display the result
print(  min(3,1,4)  )
6. Provide Function Inputs (Arguments)
Outcomes:

Provide appropriate inputs to functions by passing in appropriate arguments.
Understand and employ different argument types.
Employ optional arguments as needed.
round(18.1234567)    # try with no argument
round(18.1234567, 2  # specify the decimal places
print("Starting up....)
print()  # omit the optional argument
input("Please enter your name:")
input() # input without a prompt can be confusing
 

7. Explore Function Outputs (Return Values)
Outcomes:

Understand what it means to call a function (also referred to as executing or invoking the function).
Understand that we can refer to a function without calling it by omitting the parentheses.
len("hello")                # call the function len()
type(len("hello"))          # what type is returned when calling len()?
print( type(len("hello")) ) # call print() on the result of the type() function call

help(len)   # Sometimes, we just pass a function - but we don't want to call it
help(len()) # Oops: What happens if we pass - and call - the function?
8. Store Data in Named Variables
Outcomes:

Use variables to store and manipulate data.
Understand Python's dynamic typing.
Follow variable naming conventions.
We can store values in named variables and use those variables in reusable calculations. For example, I might use a variable named pet_weight_lbs to hold the pet weight is in pounds so I can reuse processing logic to find  overweight pets. 

pet_weight_lbs = 10.5    # a float variable
hasCreditCardOnFile = True  # True and False are capitalized
The = (equal sign) in Python is an assignment operator. We are creating a variable name (pet_weight_lbs), and using it to temporarily hold the value 10.5. Python will figure out what type pet_weight_lbs is by the value we provide. Python recognizes it and automagically makes it a float. We can say type(pet_weight_lbs) and it will return 'float'. 

Follow Variable Naming Conventions
Name your variables using whole words with underscores between them. This is the traditional Python way. Communicate clearly and always include the units information in variable names. Some of the most expensive errors have been caused by mistaking the units for a given variable. You can't leave spaces, you can't start with a number, and there's a few more rules, but if you follow most examples, you should be good. 

# We don't specify types - we just provide the data

name = "Instructor"
course_count = 6
is_experienced = True
hours_invested = 2.5

# Python determines the type from the value provided

type(name)
type(course_count)
type(is_experienced)
type(hours_invested)

Variables can hold individual values or more complex things. To create a Python list, just put your values in square brackets and separate them with commas. Now you can call the built-in function sum() on whatever your numbers list holds.  We pass in the variable by putting it inside the parentheses of the function sum(). The function returns the sum of the items in the list - either an int or a double or something else, depending on what values were in the list. 

Try defining several lists. Which built-in functions need lists and which can just handle multiple values. Use the online interpreter. Lists don't have to hold values that are all the same type - what impact does that have? Explore. 

# define some example lists
months = list(range(1,13))
numbers = [7, 6, 5, 8, 8, 4, 5, 7, 8, 6]
Optional: Add Type Hints
In Python, we don't specify the type - the Python interpreter determines it from the data we provide. This is called "dynamic typing". It makes it really easy to get started, but it can delay errors until our program is actually running. What does it mean to take the square root of "Hello" or -567.8? Being clear about our intentions helps communication. Since Python 3.5, we can add type hints - they look a lot like static types in other languages and are frequently used in industry to improve communication about what our code is supposed to do. 

They are optional - but they are quite easy to add and are  highly recommended if you want your code to look professional and up to date.  Type hints have no effect on the Python interpreter, but there are outside programs (e.g., Pyright, Mypy, Pylance) that can read them and help us help find errors. 

name:str = "Instructor"
course_count:int = 6
is_experienced:bool = True
hours_invested:float = 2.5
numbers:list = [7, 6, 5, 8, 8, 4, 5, 7, 8, 6]
Side benefit: You'll be more ready to take advantage of the new Mojo language 🔥- syntax like Python, but thousands of times faster. Be one of the first to check it out! 

9. Import Code from the Standard Library
Outcomes:

Make use of the many Python Standard Library modules.
Python comes with a broad and powerful Python Standard Library that adds additional features. There's a module for math and a module for statistics. To use them just include an import statement at the top of our Python code. To import the math module, say "import math", to import the statistics module, say "import statistics". 

# First, import modules at the top (after the docstring introduction)

import math
import statistics

# Now, we can use their functions.

# Square root
print(math.sqrt(16))

# Trigonometric functions (e.g., sine, cosine)
print(math.sin(math.pi / 2))
print(math.cos(0))

Learning the standard library takes time and experience. Python syntax can be mastered in days or weeks, but it can take months (and years) to make good use of all the free code to make projects better, faster, and more enjoyable.

If you have programming experience, spend some time this module checking out more modules from the standard library, like datetime, pathlib, csv, json, and sqlite3. 

Be More Specific
When we only require a specific function or class from a module, we can choose to import just that particular element. This is more efficient as it only loads the required component into memory. For example, if we need only the pi constant from the math module, we can import it directly using from math import pi. Similarly, to import the Path class from the pathlib module, we use from pathlib import Path. And if we need the datetime class from the datetime module, we write from datetime import datetime. Selective importing can help make code more efficient and more readable.

from math import pi
from pathlib import Path
from datetime import datetime # from datetime module, import just the datetime object
10. Create Useful Text with Formatted Strings
Outcomes:

Use f-strings to provide useful information combining text and expressions. 
You might have noticed that calling print(result) doesn't always provide useful output. We have to explain what the result represents. To print useful information, use formatted strings (f-strings). Formatted strings combine text and expressions so output has meaning. Professionals use f-strings everywhere.  

To use f-strings: Add quotes around the text and put an f directly in front of the opening quote. Use triple quotes (for multi-line strings) or quotes for a single line. Inside the string, wrap expressions in curly braces. 

course_count = 6
course_count_string = f"I have taken {course_count} course(s) towards my degree."
The easiest way to provide meaning is just to add an equals (=) after each expression (inside the curly braces).

is_experienced = True
is_experienced_string = f"{is_experienced=}"
Python IDEs and f-strings: You may be able to select a variable name (double-click) and hit the curly brace key to wrap it in curly braces. Similarly by selecting content to wrap in quotes. Sometimes, trying to be helpful, if you type a quote, it may give you two - one to open your text and one to close.  It's trying to be helpful. Be patient and try different things. Code is special. 

11. Define the Module main() Function
Outcomes: 

Understand the use of a module main() function. 
Create a useful main() for a custom module.
In Python, a module is a file (also called a script) containing Python code. It may define functions, classes, or variables. Modules help us organize our code and make it easy to reuse common utility functions in our projects.

In Python (as in other languages), professional code typically includes a main() function that encapsulates the primary functionality of the script. The main() function serves as the entry point for a program - that is, the first line of code that runs when a script is executed.

To define the main() function for our module, we:

Start with the def keyword. 
Name the function.
Add parentheses immediately after the name.
Follow the parenthesis with a (:).
Indent each statement in the function.
Keep the spacing / indentation consistent - in Python a tab is not equal to 2 spaces - or 4 spaces. Tabs and spaces are different. These things we don't see are typically called whitespace - and in Python, whitespace matters a great deal! 

def main():  # note use of def keyword and the colon (:)
  ''' The main code to execute when running this module/script/file'''
  print(course_count_string)  # indent each statement with 2 spaces
  print(is_experienced_string)
  print(hours_invested_string)
  print(numbers_string)
  print(radius_area_string)
  print(my_stats_string)
 

12. Create a Reusable Python Module
The goal is this course is to learn to write reusable, well-formatted and documented code that can be used to reliably get valuable information from data. Planning and organizing your project is an important part of every project.  

Code Organization
Python code is organized. Anything that resolves to a value is an expression (e.g. a==b), and a single executable statement is the smallest part of a Python script (program). Python is written in a file / script / module just as they did for the math module, the statistics module, and the datetime module from the standard library. If the file name is math.py, the module name is math. A package is a directory hierarchy with several modules. A library (e.g., the Python Standard Library) is a collection of modules and packages. 

Running Code
The Python interpreter runs the code. As it does, it manages information about your project. The Python interpreter has its own variables as it works. To keep them from getting confused with ours, the Python interpreter names its variables with dunders (double underscores before and after). That way, the interpreters __name__ variable doesn't get confused with any variable we might call "name" (pretty common, actually).  When you see dunders, you know that information is managed by the Python interpreter. 

Reminders
When writing Python, there's a few things to remember. 

In Python, spelling matters - it must be exact. 
In Python, capitalization matters - my_temp_f is not the same as My_Temp_F. 
In Python, spacing matters - tabs are not the same as spaces and spacing has meaning. Spacing is very important. 
Include the measuring units in the name of all numeric variables. 
Make your code look like others. Professionals uses tools to format code into standard appearance and conventions. Start now. 
Be valuable by making your team better and more functional  - be creative in your work and your problem-solving, but clear and conventional in your code. 
One Last Thing
Add the following at the end of your script.

if __name__ == "__main__":
    main()
This ensures that main() is called only when the script is executed directly, not when it's imported as a module in another script. It's a common best practice in Python. You don't have to memorize it and you don't have to type it from scratch. Just go to any professional Python script and you'll likely find it at the bottom. You can copy and paste it. Try it. The purpose will be more clear when we use our new code again in Module 2. 

Explanation (Optional)

When we run a Python script, the Python interpreter sets a  __name__ variable for each module in our running program. 

If the module is imported, its __name__ is set to the module name (e.g. "math", or "statistics").
If the module is the one that was actually run/called/executed, it is said to be the main module and the interpreter sets that module's __name__ variable to "__main__" (a special interpreter string value that indicates this is the main module that was executed). Only module gets to be "__main__".  In short, only if our script is the one being executed, then run our main() function. 
 

Some Online Experiments in Python
"""
Practicing with code comments and the built-in print function.
Dr. Case
Jan 2024
"""
print("Playing with Python")

# Single-line comment - starts with a hash
x = 22 # assigning a value to a variable
y = 77 # assigning a value to another variable

# calling built-in print() function with one argument is easy
print(x)
print(y)

print("That's nice, but not very helpful. Which is which?")
print()

# call print() with many arguments - just separate them by commas
print("x is equal to ", x, " and y is equal to ", y)
print("That's better, but a lot of work. Anything better?")
print()
# printing with an f-string or formatted string
# (like the cool kids do)
# just add an f just before the opening quote
# now you can insert Python expressions wherever you like
# Just wrap them in curly braces.
print(f"x is {x} and y is {y}.")
print()
print("Nice! Anything else I should try?\n") # \n adds a new line
# To be SUPER cool, try this bit of syntactic sugar
# At the end, just INSIDE a set of curly braces, add =
# It will AUTOMAGICALLY pretty print the name and value!
print(f"{x=}, {y=}")
print("Dang. That's fun! All done playing for now!")
image.png

**Optional - Video Excerpts on Key Topics**
You don't need ALL of these videos yet - but these excerpts are great overviews of key topics. Share your suggestions as you find them. 

PYTHON FOR DATA SCIENCE, AI & DEVELOPMENT (IBM Video)
7:35:08 TypesLinks to an external site.


7:38:11 Expressions and VariablesLinks to an external site.


 

F-Strings

From **10 Python Shortcuts** You Need To Know - #1 is f-strings!
https://www.youtube.com/watch?v=CssrFJGH_dU&t=98sLinks to an external site.

 
You don't need ALL of these videos yet - but these excerpts are great overviews of key topics. Share your suggestions as you find them. 

**PYTHON FOR DATA SCIENCE, AI & DEVELOPMENT** (IBM Video)
7:35:08 TypesLinks to an external site.


7:38:11 Expressions and VariablesLinks to an external site.


 

F-Strings

From 10 Python Shortcuts You Need To Know - #1 is f-strings!
https://www.youtube.com/watch?v=CssrFJGH_dU&t=98sLinks to an external site.

 

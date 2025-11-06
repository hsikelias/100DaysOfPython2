# FUNCTIONS WITH OUTPUTS

# lets recall: Our first thing we learn about functions is its syntax

# def my_function():
  # Do this
  # Then this
  # Finally this


## Next we learnt to use, function with input
# def my_function(something)
  # Do this with something
  # Then do this
  # Finally do this

# my_function(123)  So the something is an input which we can passover here, rn its 123


# Functions with Outputs

def my_function(): #No parameters here
  result = 3*2  
  return result  # this is output keyword, here we output the result

my_function()   # when we call this function, it runs and sends an output of the result


# you can also define a variable to a function, the variable stores the output of the function. 


# def my_function():
#   return 3 * 2
# output = my_function2()


# -----------------------------------------------------------------------------------------------------------

# takes the first name and last name of the user and makes it text case, first character is capitalized rest all lower case. 


'''
THIS IS WHAT I DID


def format_name():
  f_name = input("Enter your first name: ").lower()
  l_name = input("Enter your last name: ").lower()
  f_name_list = list(f_name)
  l_name_list = list(l_name)
  index = 0 

  f_name_list[index] = f_name_list[index].upper()
  l_name_list[index] = l_name_list[index].upper()

  new_f_name = "".join(f_name_list)
  new_l_name = "".join(l_name_list)

  print(f"Hello {new_f_name} {new_l_name}")
format_name()

'''


# ANGELAS VIDEO

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  print(f"{formated_f_name} {formated_l_name}")
format_name('lekish sai','podili')

# Reflection: I mean this is obviously much shorter i knew something like .title existed but I just wanted to build everything from scratch. 


# PRINT VS RETURN

def function_1(text):
  return text + text #Ouput = helohelo

def function_2(text):
  return text.title()

output = function_2(function_1("Hello"))
print(output)

# look at how we are able to move stuff around with return but its not possible in print

# MULTIPLE RETURN STATEMENTS

## we usually think of return statements as things that show up at the end of a certain function. But what if we have multiple return statement??





# Docstrings: A way for us to create bits of documentation while we code our functions. Like for len() if we hoover over that function we get a documentation pop up that explains what the function does. To do the same thing for our functions is called Docstrings

# the doctsrings go under the first indented line and whatever u say should go between """ """

def format_name(f_name, l_name):
  """ Take a first and last name and format ot tp return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You did not provide valid input" # terminates the function early if the user enters an empty string.
  
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return (f"{formated_f_name} {formated_l_name}")

print(format_name(input("What is your first name?"), input("What is your last name?")))

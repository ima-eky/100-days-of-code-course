def logging_decorator(function):
  def wrapper_function(*args,**kwargs):
    name_of_function=f"{function.__name__}"
    arguments_given=f"{args}"
    output=function(args[0],args[1],args[2],args[3])
    print(f"You called {name_of_function}{arguments_given}\nIt returned {output}")
  return wrapper_function


# Use the decorator 👇
@logging_decorator
def add_numbers(a,b,c,d):
    return a + b+ c+ d
add_numbers(2,3,4,5)
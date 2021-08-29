# define an Exception
# give exception object a name
class NameError(Exception):
    pass

def input_user_name1():
    user_name=input("enter your name")
    if len(user_name)==0:
        raise NameError("The user name can't be empty!")

    print(user_name)

try:
    input_user_name1()
except NameError as e:
    print("NameError: "+ str(e))
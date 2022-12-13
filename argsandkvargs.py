# *args and **kwargs
# *vars and **kvars

def fuction_1(*args):
    print(type(args)) #tuple
    if(len(args)==3):
       print("The name of the student is", args[0], "and age is", args[1], "and rollno is",args[2])
    else:
        print("Th name of the student is", args[0], "and age is", args[1])

function_1("harry",22,3455)



#for key value pair we used kwargs
def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key,value)

marklist={"Harry":100,"Rohan Das":97}
printmarks(**marklist)
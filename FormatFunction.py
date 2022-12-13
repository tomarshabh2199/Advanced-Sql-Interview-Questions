users=['shubham','prince','rakesh','manoj']

computer=['rasberry pi','hp','dell']

for i in range(0, len(users)):
    print("Computer used by",users[i],"is",computer[i])


for i in range(0,len(users)):
    template ="Computer used by {0} is {1}"
    template ="Computer used by {1} is {0}"
    print(template.format(users[i], computer[i]))
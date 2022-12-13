try:
    open("this.txt")
except Exception as e:
    pass
    print(e)


try:
    file=open("this.txt")

except EOFError as eof:
    print("eof error")

except IOError as e:
    print("IOError")

finally:
    print("always printed")


try:
    print("Throw error")

except Exception as e:
    print("Exception occured")
    
else:
    print("Will run only there is no exception")

finally:
    print("every case printed")
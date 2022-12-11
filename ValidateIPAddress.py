#write a function to validate if a string is a valid ip address or not
# a valid ip address should be in form of x1.x2.x3.x4 where x1,x2,x3,x4
# should be numbers between 0 and 255
# 4 digits, its a digit, 0 and 255

def isValid_ip(s):
    ip_list=s.split('.')
    if len(ip_list)!=4:
        return False
    for n in ip_list:
        if n.isdigit()==False:
            return False
        if int(n)<0 or int(n)>255:
            return False    
    return True
 
print(isValid_ip('255.23.12.23'))
print(isValid_ip('255.13.09.12'))
print(isValid_ip('255.23.12.23'))


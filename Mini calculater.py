import math
def cal(x,y,z):
    if(x==1):
        print("The addition is :",y+z)
    elif(x==2):
        print("Subraction is :",y-z)
    elif(x==3):
        print("Multiplicatin is :",a*b)
    elif(x==4):
        print("Division is :",a/b)
    elif(x==5):
        print("Sine of the number is:",math.sin(y))
    elif(x==6):
        print("Cos of the number is ",math.cos(y))
    elif(x==7):
        print("Tan of the number is ",math.tan(y))
        
        
print("****MINI CALCULATOR****")
print("1.add , 2.sub , 3.mul , 4.div , 5.sin , 6.cos , 7.tan")
n=int(input("Enter your choice: "))
l=[1,2,3,4]
l1=[5,6,7]
if n in l:
    a=int(input("Enter the value one: "))
    b=int(input("Enter the value two: "))
    cal(n,a,b)

elif n in l1:
    v=int(input("enter th value: "))
    cal(n,v,0)
    
else:
    print("enter th correct value")
    
    
    
    

        
    

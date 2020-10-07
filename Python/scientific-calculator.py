#Basic python scientific calculator using terminal
import math

class Calculator(object):
    def add(self,num1,num2):
        answer = num1 + num2
        print("Sum = ",answer)
    def sub(self,num1,num2):
        answer = num1 - num2
        print("Difference = ",answer)
    def mul(self,num1,num2):
        answer = num1 * num2
        print("Product = ",answer)
    def div(self,num1,num2):
        answer = num1 / num2
        print("Quotient = ",answer)
    def sinrad(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2
        answer = math.sin(num)
        print("Sine (%f) in rad  = %f" %(num,answer))
    def cosrad(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2
        answer = math.cos(num)
        print("Cos (%f) in rad  = %f" %(num,answer))
    def tanrad(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2
        answer = math.tan(num)
        print("Tan (%f) in rad = %f" %(num,answer))
    def cosecrad(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2
        answer = 1/(math.sin(num))
        print("Cosec (%f) in rad  = %f" %(num,answer))
    def secrad(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2
        answer = 1/(math.cos(num))
        print("Sec (%f) in rad  = %f" %(num,answer))
    def cotrad(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = 1/(math.tan(num))
        print("Cot(%f) in rad = %f" %(num,answer))
    def sindeg(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.sin(math.radians(num))
        print("Sin(%f) in degrees = %f" %(num,answer))
    def cosdeg(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.cos(math.radians(num))
        print("Cos(%f) in degrees = %f" %(num,answer))
    def tandeg(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.tan(math.radians(num))
        print("Tan(%f) in degrees = %f" %(num,answer))
    def cosecdeg(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = 1/(math.sin(math.radians(num)))
        print("Cosec(%f) in degrees = %f" %(num,answer))
    def secdeg(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = 1/(math.cos(math.radians(num)))
        print("Sec(%f) in degrees = %f" %(num,answer))
    def cotdeg(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = 1/(math.tan(math.radians(num)))
        print("Cot(%f) in degrees = %f" %(num,answer))
    def ln(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.log(num)
        print("ln(%f) = %f" %(num,answer))
    def logten(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.log10(num)
        print("log10(%f) = %f" %(num,answer))
    def logbasex(self,num,x):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.log(num,x)
        print("log base(%f)(%f) = %f" %(x,num,answer))
    def squareroot(self,num):
        if num == "pi":
            num = math.pi
        elif num == "pi/2":
            num = math.pi/2
        elif num == "3*pi/2":
            num = (3*math.pi)/2        
        answer = math.sqrt(num)
        print("Square Root(%f) = %f " %(num,answer))
    def pie(self):
        print( 'pi = ',math.pi)
    def powerof(self,num,raiseby):
        answer = num**raiseby
        print("%f ^ (%f) = %f" %(num,raiseby,answer) )

calc = Calculator()
print("Welcome to this scientific calculator!")
print("Here's a list of choices")
print('*'*50)
print("1 : Addition  \t\t   12 : Sine in degrees")
print("2 : Subtraction \t   13 : Cosine in degrees")
print("3 : Multiplication\t   14 : Tan in degrees")
print("4 : Division  \t\t   15 : Cosecant in degrees")
print("5 : Sine in radians\t   16 : Secant in degrees")
print("6 : Cosine in radians\t   17 : Cot in degrees")
print("7 : Tan in radians\t   18 : Natural log")
print("8 : Cosecant in radians    19 : Base 10 log")
print("9 : Secant in radians\t   20 : Log base 'x'")
print("10 : Cot in radians\t   21 : Square root")
print("11 : pi \t\t   22 : Power of")
print('*'*50)

while True:
    try:
        choice = int(input('enter a number of your choice from the above list : '))
    except:
        print("Enter a valid number")
    if choice == 1:
        n1 = float(input('enter the first number to add : '))
        n2 = float(input('enter the second number to add : '))
        calc.add(n1,n2)
    elif choice == 2:
        n1 = float(input('enter the first number to subtract : '))
        n2 = float(input('enter the second number to subtract : '))
        calc.sub(n1,n2)
    elif choice == 3:
        n1 = float(input('enter the first number to multiply : '))
        n2 = float(input('enter the second number to multiply : '))
        calc.mul(n1,n2)
    elif choice == 4:
        n1 = float(input('enter the first number to divide : '))
        n2 = float(input('enter the second number to divide : '))
        calc.div(n1,n2)
    elif choice == 5:
        n = input('enter a number to find its sine in rad: ')
        calc.sinrad(n)
    elif choice == 6:
        n = input('enter a number to find its cos in rad: ')
        calc.cosrad(n)
    elif choice == 7:
        n = input('enter a number to find its tan in rad : ')
        calc.tanrad(n)
    elif choice == 8:
        n = input('enter a number to find its cosec in rad : ')
        calc.cosecrad(n)
    elif choice == 9:
        n = input('enter a number to find its sec in rad : ')
        calc.secrad(n)
    elif choice == 10:
        n = input('enter a number to find its cot in rad : ')
        calc.cotrad(n)
    elif choice == 11:
        calc.pie()
    elif choice == 12:
        n = input('enter a number to find its sine in deg : ')
        calc.sindeg(n)
    elif choice == 13:
        n = input('enter a number to find its cos in deg : ')
        calc.cosdeg(n)
    elif choice == 14:
        n = input('enter a number to find its tan in deg : ')
        calc.tandeg(n)
    elif choice == 15:
        n = input('enter a number to find its cosec in deg : ')
        calc.cosecdeg(n)
    elif choice == 16:
        n = input('enter a number to find its sec in deg : ')
        calc.secdeg(n)
    elif choice == 17:
        n = input('enter a number to find its cot in deg : ')
        calc.cotdeg(n)
    elif choice == 18:
        n = input('enter a number to find its natural deg : ')
        calc.ln(n)
    elif choice == 19:
        n = float(input('enter a number to find its log to base 10 : '))
        calc.logten(n)
    elif choice == 22:
        n = float(input('enter a number  : '))
        po = float(input('enter its power : '))
        calc.powerof(n,po)
    elif choice == 21:
        n = float(input('enter a number to find its square root : '))
        calc.squareroot(n)
    elif choice == 20:
        base = float(input('enter base value : '))
        n = float(input('enter a number to find its log to the given base value: '))
        calc.logbasex(n,base)
    else:
        print("WARNING : Enter a valid input from the list above")
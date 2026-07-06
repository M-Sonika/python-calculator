def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
   return (a*b)
def divide(a,b):
    if b==0:
       return("Error: Cannot divide by zero.")
    return(a/b)
def percentage(a,b):
   if b==0:
       return("Error: Cannot divide by zero.")
   return(a/b)*100
def power(a,b):
    return a ** b
import math
def square_root(a):
    if a<0:
        return "cannot find the square root of negative number"
    return math.sqrt(a)
def modulus(a,b):
    return a%b
while True:
    print("Welcome to python calculator")
    print("1. Addition")
    print("2. subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage ")
    print("6. power")
    print("7. Square root")
    print("8. Modulus")
    choice = input("choose an operation(1-8):")
    try:
      num1=float(input("Enter the first number:"))
      num2=float(input("Enter the second number:"))
    except ValueError:
      print("Invalid input! please enter the numbers only")
      continue
    if choice == "1":
        result = add(num1,num2)
        print("the sum is:",round(result,2))
    elif choice == "2":
        result= subtract(num1,num2)
        print("the difference is:",round(result,2))

    elif choice == "3":
        result = multiply(num1,num2)
        print("The product is:", round(result,2))
    elif choice == "4":
          if num2 == 0:
            print("Error: Cannot divide by zero.")
          else:
             result = divide(num1,num2)
             print("The quotient is:", round(result,2))
    elif choice ==  "5":
         result = percentage(num1,num2)
         print("percentage is:",round(result,2),"%")
    elif choice == "6":
        result = power(num1,num2)
        print("Result is:", round(result,2))    
    elif choice == "7":
        num=float(input("enter a number"))
        result = square_root(num)
        print("Square root is:", round(result,2))  
    elif choice == "8":
        result = modulus(num1,num2)
        print("The Remainder is:",round(result,2))  
    else:
        print("invalid choice")
    again = input("Do you want to calculate again?(yes/no):")
    if again.lower() != "yes":
         print("Thank you for using the calculator!")
         break

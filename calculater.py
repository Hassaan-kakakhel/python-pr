num1= int(input("enter first number:"))
num2 = int(input("enter second number:"))
operator = input("enter operator (+, -, *, /):")
print("WELCOME TO CALCULATOR")
def calculate(num1, num2, operator):
  
        
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
       
answer = calculate(num1, num2, operator)        
print(f"the answer is {answer}")

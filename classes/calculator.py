
class Calculator:
    def __init__(self):
        pass
        
    #addition function
    def addition(self, first_num, second_num):
        if not isinstance(first_num,(int, float))or not isinstance(second_num,(int,float)):
            raise TypeError("Inputs must be number!")
        else:
            return round(first_num + second_num, 2)
    #subtraction function
    def subtract(self, first_num, second_num):
        return round(first_num - second_num, 2)

    #multiply function
    def multiply(self, first_num, second_num):
        return round(first_num * second_num,2)

    #divide function
    def divide(self, first_num, second_num):
        if(second_num == 0):
            raise ZeroDivisionError("Error! cannot divide by zero")
        else:
            return  round(first_num / second_num, 2)

#function for getting valid number
def get_number(prompt):  # pragma:no cover
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Try again!")

#function for getting valid operator 
def get_operator(prompt):  # pragma:no cover
    while True:
        valid_operators = ['+', '-', '*', '/']
        op = input(prompt)
        if op in valid_operators:
            return op
        else:
            print("Invalid operator! Choose again.")
            
if __name__ == "__main__":  # pragma:no cover

    first_number = get_number("Enter a number: ")
    operator_choice = get_operator("Enter the operation (+, -, /, *): ")
    second_number = get_number("Enter another number: ")

    #create an instance of Calculator object
    calc = Calculator()
#declare a dictionary for operation
    list_operation = {'+': calc.addition, '-': calc.subtract, '*': calc.multiply, '/': calc.divide}

# print the results
    if operator_choice in list_operation:
        print(f"{first_number} {operator_choice} {second_number} is {list_operation.get(operator_choice)(first_number, second_number)}")
   


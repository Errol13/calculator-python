

#addition function
def addition(first_num, second_num):
    if not isinstance(first_num,(int, float))or not isinstance(second_num,(int,float)):
        raise TypeError("Inputs must be number!")
    else:
        return first_num + second_num
#subtraction function
def subtract(first_num, second_num):
    return first_num - second_num

#multiply function
def multiply(first_num, second_num):
    return first_num * second_num

#divide function
def divide(first_num, second_num):
    if(second_num == 0):
        raise ZeroDivisionError("Error! cannot divide by zero")
    else:
        return first_num / second_num

#function for getting valid number
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Try again!")

#function for getting valid operator 
def get_operator(prompt):
    while True:
        valid_operators = ['+', '-', '*', '/']
        op = input(prompt)
        if op in valid_operators:
            return op
        else:
            print("Invalid operator! Choose again.")
            
if __name__ == "__main__":

    first_number = get_number("Enter a number: ")
    operator_choice = get_operator("Enter the operation (+, -, /, *):")
    second_number = get_number("Enter another number: ")

#declare a dictionary for operation
    list_operation = {'+': addition, '-': subtract, '*': multiply, '/': divide}

# print the results
    if operator_choice in list_operation:
        print(f"{first_number} {operator_choice} {second_number} is {list_operation.get(operator_choice)(first_number, second_number)}")
   


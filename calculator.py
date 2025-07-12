

#addition function
def addition(first_num, second_num):
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
        return "Error! cannot divide by zero!"
    else:
        return first_num / second_num

if __name__ == "__main__":

    
    first_number = int(input("Enter a number: "))
    operator_choice = input("Enter the operation (+, -, /, *):")
    second_number = int(input("Enter another number: "))

#declare a dictionary for operation
    list_operation = {'+': addition, '-': subtract, '*': multiply, '/': divide}

# call the function and print the results
    print(f"{first_number} {operator_choice} {second_number} is {list_operation.get(operator_choice)(first_number, second_number)}")


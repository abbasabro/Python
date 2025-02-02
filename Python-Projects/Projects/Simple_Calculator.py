
def calculation(operator , operand_01 , operand_02):
    if operator == '+':
        return operand_01 + operand_02
    elif operator == '-':
        return operand_01 - operand_02
    elif operator == '*':
        return operand_01 * operand_02
    elif operator == '/':
        return check_division(operand_01,operand_02)
    else :
        print("Invalid Operaor!")


def check_division(operand_01 , operand_02):
    try:
        return operand_01 / operand_02
    except ZeroDivisionError:
        print("Cannot Divide By zero")


operator = input("Enter Operation to Perform (+,-,*,/) : ")
operand_01 = int(input("Enter First Operand : "))
operand_02 = int(input("Enter Second Operand : "))

print(calculation(operator,operand_01,operand_02))
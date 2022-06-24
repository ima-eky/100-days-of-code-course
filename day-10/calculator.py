def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


mathematical_operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,

}


def calculator():
    num1 = int(input("What is the first number?:"))
    for symbol in mathematical_operation:
        print(symbol)
    should_continue = True
    while (should_continue):
        operation_symbol = input('Pick an operation:')
        num2 = int(input("What is the next  number?:"))
        task = mathematical_operation[operation_symbol]
        answer = task(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        still_continue = input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation:")
        if still_continue == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
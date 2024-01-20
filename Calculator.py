class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self.result

    def subtract(self, number):
        self.result -= number
        return self.result

    def multiply(self, number):
        self.result *= number
        return self.result

    def divide(self, number):
        if number == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result /= number
        return self.result


calculator = Calculator()
print("Enter the first number: ")
number1 = float(input())

while True:
    print("Choose operation: +, -, *, /")
    operation = input()

    if operation == '/':
        try:
            print("Enter the second number: ")
            number2 = float(input())
            result = calculator.divide(number2)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)
            continue

    else:
        print("Enter the second number: ")
        number2 = float(input())

        if operation == '+':
            result = calculator.add(number2)
        elif operation == '-':
            result = calculator.subtract(number2)
        elif operation == '*':
            result = calculator.multiply(number2)

        print(f"Result: {result}")

    print("Do you want to continue calculations? Y/N")
    choice = input()
    if choice.lower() != 'y':
        break
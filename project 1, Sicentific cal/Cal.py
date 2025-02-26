import math
# If you know how to use a Class
class Cal:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    def mod(self):
        return self.num1 % self.num2
    def power(self):
        return self.num1 ** self.num2
    def root(self):
        return math.sqrt(self.num1)
    def log(self):
        return math.log(self.num1)
    def sin(self):
        return math.sin(self.num1)
    def cos(self):
        return math.cos(self.num1)
    def tan(self):
        return math.tan(self.num1)

# If you don't know how to use a Class
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def power(a, b):
    return a ** b
def root(a):
    return math.sqrt(a)
def log(a):
    return math.log(a)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)


# User input and function calling(You have to compleate this part)
def class_metord(oparator, num_1, num_2):
    o = oparator
    num_1 = num_1
    num_2 = num_2
    cal = Cal(num_1, num_2)
    if o == "+":
        print(cal.add())
    elif o == "-":
        print(cal.sub())
    elif o == "/":
        print(cal.div())
    elif o == "*":
        print(cal.mul())
    elif o == "**":
        print(cal.power())
    elif o == "%":
        print(cal.mod())
    elif o == "squer root":
        print(cal.root())
    elif o == "sin":
        print(cal.sin())
    elif o == "cos":
        print(cal.cos())
    elif o == "tan":
        print(cal.tan())
    elif o == "log":
        print(cal.log())
    else:
        print("Invalid oparation try again!!")


def non_class_metord(oparater, num_1, num_2):
    o = oparater
    num_1 = num_1
    num_2 = num_2
    if o == "+":
        print(add(num_1, num_2))
    elif o == "-":
        print(sub(num_1, num_2))
    elif o == "/":
        print(div(num_1, num_2))
    elif o == "*":
        print(mul(num_1, num_2))
    elif o == "**":
        print(power(num_1, num_2))
    elif o == "%":
        print(mod(num_1, num_2))
    elif o == "squer root":
        print(root(num_1))
    elif o == "sin":
        print(sin(num_1))
    elif o == "cos":
        print(cos(num_1))
    elif o == "tan":
        print(tan(num_1))
    elif o == "log":
        print(log(num_1))
    else:
        print("Invalid oparation try again!!")


if __name__ == "__main__":
    while True:
        print("Enter the operation you want to perform(+, -, /, *, %, **, squer root, cos, sin, tan, log) exit() to exit: ")
        oparation = input()
        if oparation == "exit()":
            print("Hope to see you again. Bye for now!")
            break
        else:
            pass
        print("Enter two numbers (for cos, sin, tan, log enter only one, sencond one no counted): ")
        x = input("num_1: ")
        y = input("num_2: ")
        if x.isdigit() and y.isdigit():
            x, y = int(x), int(y)
        else:
            print("Numbers must be numbers")
            continue
        # remove the hash tag and space of motord needed
        class_metord(oparation, x, y)
        # non_class_metord(oparation, x, y)

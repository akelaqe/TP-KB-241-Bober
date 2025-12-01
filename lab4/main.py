import math

def priority(op):
    priorities = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    return priorities.get(op, 0)

def tokenize(expression):
    tokens = []
    number = ""

    for char in expression:
        if char.isdigit() or char == '.':  
            number += char
        else:
            if number:
                tokens.append(number)
                number = ""
            if char.strip():
                tokens.append(char)

    if number:
        tokens.append(number)

    return tokens


def to_rpn(tokens):
    output = []
    stack = []

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  

        else:  
            while stack and priority(stack[-1]) >= priority(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def evaluate_rpn(rpn):
    stack = []

    for token in rpn:
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            elif token == '^': stack.append(a ** b)

    return stack[0]


expression = input("Введіть математичний вираз: ")
tokens = tokenize(expression.replace(" ", ""))

rpn = to_rpn(tokens)
print("ЗПЗ:", " ".join(rpn))

result = evaluate_rpn(rpn)
print("Результат:", result)
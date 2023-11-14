def evaluate_expression(expr):
    elements = []
    current_number = ''
    for char in expr:
        if char.isdigit():
            current_number += char
        elif char in ('+', '-', '*', '/'):
            if current_number:
                elements.append(current_number)
                current_number = ''
            elements.append(char)
        elif char != ' ':
            return "Caractère invalide : " + str(char)
    if current_number:
        elements.append(current_number)
        
    i = 0
    while i < len(elements):
        if elements[i] in ('*', '/'):
            operator = elements[i]
            leftOp = int(elements[i - 1])
            rightOp = int(elements[i + 1])

            if operator == '*':
                elements[i - 1:i + 2] = [str(leftOp * rightOp)]
            else:
                if rightOp != 0:
                    elements[i - 1:i + 2] = [str(leftOp / rightOp)]
                else:
                    return "Division par zéro impossible"
        else:
            i += 1
            
    result = int(elements[0])
    i = 1
    while i < len(elements):
        operator = elements[i]
        operand = int(elements[i + 1])

        if operator == '+':
            result += operand
        else:
            result -= operand
        i += 2

    return result

operation = input("Saisissez une opération mathématique (par ex 8*56-32+1) : ")
result = evaluate_expression(operation)
print("Résultat : " + str(result))
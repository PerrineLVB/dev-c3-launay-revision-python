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
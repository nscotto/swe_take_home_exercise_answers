import re

def parse_line(line):
    """
    Parse a line into tokens.
    :param line: str, line
    :return: list of tokens (str)
    """
    ops_re = re.compile(r'(\+|-|\*|/|\(|\))')
    spaced_line = ops_re.sub(r' \1 ', line)
    return spaced_line.strip().split()


def process(operator, a, b):
    """
    Compute operator(a, b)

    :param operator: str
    :param a: float
    :param b: float

    :return: float

    :raise RuntimeWarning: if the operator is not supported
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        raise RuntimeWarning()


def prefix_eval(line):
    """
    Exercice 1
    Prefix evaluation of line.

    :param line: str, operation in prefix notation

    :return: float

    :raise RuntimeWarning: if the operator is not supported
    """
    ops = parse_line(line)
    operands = []
    for elmt in reversed(ops):
        if elmt.isnumeric():
            operands.append(float(elmt))
        else:
            operands.append(process(elmt, operands.pop(), operands.pop()))
    
    res = operands[0]
    return int(res) if res.is_integer() else res 


def infix_eval(line):
    """
    Exercice 2
    Infix evaluation of line.

    :param line: str, operation in infix notation

    :return: float

    :raise RuntimeWarning: if the operator is not supported are parenthesis 
        are not unmatched
    """
    ops = parse_line(line)
    operands = []
    operators = []
    precedance = {'(': -1, '+': 0, '-': 0, '*': 1, '/': 1}

    print(ops)

    for elmt in ops:
        print('el', elmt)
        if elmt.isnumeric():
            operands.append(float(elmt))
        elif elmt == '(':
            operators.append(elmt)
        elif elmt == ')':
            while operators and operators[-1] != '(':
                b, a = operands.pop(), operands.pop()
                operands.append(
                    process(operators.pop(), a, b)
                )
            if operators:
                operators.pop()
            else:
                 raise RuntimeWarning('Unmatched parenthesis!')
        else:
            while operators and precedance[operators[-1]] >= precedance[elmt]:
                b, a = operands.pop(), operands.pop()
                operands.append(
                    process(operators.pop(), a, b)
                )
            operators.append(elmt)
    
    while operators:
        b, a = operands.pop(), operands.pop()
        operands.append(
            process(operators.pop(), a, b)
        )
        
    res = operands[0]
    return int(res) if res.is_integer() else res


if __name__ == "__main__":
    exp = [
        "3",
        "+ 1 2",
        "+ 1 * 2 3",
        "+ * 1 2 3",
        "- / 10 + 1 1 * 1 2",
        "- 0 3",
        "/ 3 2"
    ]
    print('Prefix:')
    print('\n'.join(f'{op}: {prefix_eval(op)}' for op in exp))
    exp = [
        "( 1 + 2 )",
        "( 1 + ( 2 * 3 ) )",
        "( ( 1 * 2 ) + 3 )",
        "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"
    ]
    print('Infix:')
    print('\n'.join(f'{op}: {infix_eval(op)}' for op in exp))


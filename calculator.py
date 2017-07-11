"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(expression):
    """ Evaluate polish expressions. """
 
    #turn expression into a list of strings
    expression = expression.split()
    #pop off the last, right-most number of the expression
    operand2 = int(expression.pop())

    #while the expression is True, pop off the next, right-most number and operator
    while expression:

        operand1 = int(expression.pop())

        operator = expression.pop()

        #check to see which operator to use, reassign operand 2 as the result of operand1 and operand 2
        if operator == "+":
            operand2 = operand1 + operand2

        elif operator == "-":
            operand2 = operand1 - operand2

        elif operator == "*":
            operand2 = operand1 * operand2

        elif operator == "/":
            operand2 = operand1/operand2

    #after the last number and last operator are evaluated, return operand2, the result of all calculations
    return operand2



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"





import operator


def arithmetic_operation(operation):
    type_operation = {'+': operator.add, '-': operator.sub,
                      '/': operator.truediv, '*': operator.mul}

    def func(x, y):
        return type_operation[operation](x, y)
    return func


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))

from day7.main1 import result


def add(x,y):
    return x+y




def concatenate(x,y):
    return str(x) + str(y)

def operate(operation , x,y):
 """
   :param  This is a operation that needs to be performed:
   :param  x the first operand:
   :param  y  the second operand:
   :return: The result of th operation
 """
 return operation(x,y)




result_sum = operate(add, 3,5)
result_concatenate = operate(concatenate,3,5)
print("Result of sum:" , result_sum)
print("Result of :" , result_concatenate)

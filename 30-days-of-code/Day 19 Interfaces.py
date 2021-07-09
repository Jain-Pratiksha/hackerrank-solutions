class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    
    def divisorSum(self, n):
        result = int()
        for i in range(1, 1001): #1001 since numbers can be till 1000
            if(n % i is 0):
                result += i
        return result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

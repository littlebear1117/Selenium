'''
Alex helped to create this class

03/10/2017 Add unit test:
1. Add
'''

## Test a python class

class Calculate(object):
    # May or may not define "zeor":
    #zero = 90

    def add(self, x, y):
      return x + y + self.zero

if __name__ == '__main__':
    calc = Calculate()
    calc.zero = 9
    result = calc.add(2, 2)
    print ("Result is: ", result)

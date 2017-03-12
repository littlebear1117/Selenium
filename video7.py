# Functions
# https://www.youtube.com/watch?v=3DEHhI4-Ki4

def doSomething():
    print ("Hello Wolrd")

def getList(max):
    x = list(range(max))
    for i in x:
        x[i] = i * 5
    return x

def printPerson(name = "Unkown", age = 0):
    print ("The person is named %s " % name)
    print ("They are %d years old" % age)

print ("Start the program....")
doSomething()

myList = getList(59)

print (myList)


printPerson()

h = 50
if h > 50 :
    printPerson("Andrew", 55)
else:
    printPerson("Sherry", 52)

# Error handling
# KISS - keep it simple / stupid

def doSomething(number):
    try:
        x = 5
        y = x / number
        print (y)
    except OSError:
        print ("OS Error")
    except RuntimeError:
        pass
    # except ZeroDivisionError:
    #     pass
    #     print ("Please do not dev by zero")

    except Exception as e:
        print ("something went to boom: %s" % e)
    finally:
        print ("Finally I geto to run")
print ("Starting program")
doSomething(0)
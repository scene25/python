
def greet(szName):
    if(len(szName) <= 0):
        return
    szOutput = "hello " + szName
    print(szOutput)
    
greet("bob");
greet("john");
greet("");

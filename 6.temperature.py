
def PrintCheckTemperature(InputVal):
    nValue = int(InputVal)
    nCheckTemperature = 72
    if(nValue >= nCheckTemperature):
        print("too hot");
    else:
        print("too cold");
        
CurTemperature = input("input temperature..\n")
PrintCheckTemperature(CurTemperature)

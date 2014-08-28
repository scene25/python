
def PrintCheckTemperature(nValue):
    nCheckTemperature = 72
    if(nValue >= nCheckTemperature):
        print("too hot");
    else:
        print("too cold");
        
PrintCheckTemperature(30)
PrintCheckTemperature(70)
PrintCheckTemperature(72)
PrintCheckTemperature(80)   

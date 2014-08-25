data = (2, 45, 55, 200, -100, 99, 37, 10284)
listResult = []

for i in data:
    if(i % 3 == 0):
        listResult.append(i)
        
for nValue in listResult:
    print(nValue)
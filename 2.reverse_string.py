test = "this is test string"

nLength = len(test);
szOutput = ""

for i in range(nLength-1, -1, -1):
    szOutput +=  test[i]

print(szOutput)
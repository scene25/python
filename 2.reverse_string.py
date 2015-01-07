test = "this is test string"

'''
nLength = len(test);

for i in range(nLength-1, -1, -1):
    szOutput +=  test[i]
'''

szOutput = test[::-1]

print(szOutput)
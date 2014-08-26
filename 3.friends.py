friends = ['john', 'pat', 'gary', 'michael']
szOutput = ""
nIndex = 0

for szName in friends:
    szOutput = "No. %d is %s" % (nIndex+1, friends[nIndex])
    nIndex += 1
    print(szOutput)


'''
output:
    No. 1 is john
    No. 2 is pat
    No. 3 is gary
    No. 4 is michael
'''
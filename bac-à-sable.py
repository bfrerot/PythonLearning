def test(lst):
    del lst[3]
    lst[3] = 'ram'
    return lst
testlist=[0,1,2,3,4]
print (test(testlist))
import random
def test_only_evens(list):
    even_numbers = []
    for sublist in list:
        for i in sublist:
            if i%2 == 0:
                even_numbers.append(i)
    return even_numbers

def test_sub(lst, start, end):
    return lst(start, end)

def sub(lst, start, end):
    lst=[1,2,3,4,5,6,7,8,]
    print(sub(lst,2, 5))

def test_concat(lst1,lst2):
    ans = []
    for i in lst1:
        ans.append(i)
    for i in lst2:
        ans.append(i)
    return ans

def concat(lst1,lst2):
    lst1=[10,20,30,40]
    lst2=[50,60,70,80]
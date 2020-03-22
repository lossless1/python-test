"""
This is comment
"""

#this is too

# myvar = 123
# print myvar

arr = [1, ["first"]]
print arr[0]


# str = "First string"
# #str[3] = "allow"
# print str[2]


# kortej = ("a", "b", "c", "d")


# print kortej[-1:]


# print "Name: %(name)s, Surname: %(surname)s" % {"name": "Vladimir", "surname": "Saakian"}

# rangeList = range(50)
# print rangeList

# for number in rangeList:
#     print number


num = 3
lists = (2, 3, 4, 5)

if num in lists:
    print num


def printString(string):
    print "This is string: " + string


def printNumber(x): return print x


printString("Hello")
printNumber(100)

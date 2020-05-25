
"""
    This algorithm uses three index variables: first , last , and middle . The first and last
    variables mark the boundaries of the portion of the array currently being searched. They
    are initialized with the subscripts of the list’s first and last elements. The subscript of the
    element halfway between first and last is calculated and stored in the middle variable.
    If the element in the middle of the array does not contain the search value, the first or
    last variables are adjusted so that only the top or bottom half of the list is searched
    during the next iteration. This cuts the portion of the array being searched in half each time
    the loop fails to locate the search value.
"""



originalList = [7, 2, 9, 4, 6, 5, 1, 8, 3,10]
myList = sorted(originalList)
print("\nThe original list is {}".format(originalList))
print("\nThe sorted list is {}".format(myList))
first = 0
last = len(myList) - 1
position = -1
found = False


num = int(input("\nEnter the number you want to search: "))

while (not found and first <= last):
    middle = (first + last)//2  
    if(myList[middle] == num):
        found = True
        position = middle
    elif (myList[middle] > num):
        last = middle - 1
    else:
        first = middle + 1

if position == -1:
    print("\nNot found.")
else:
    print("\nThe number u entered, {} , has been found".format(myList[position]) )

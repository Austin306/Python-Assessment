class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))


def BinarSearch(list, l, r, x):

    # Check base case
    if r >= l:

        mid = (l + r)//2

        # If element is present at the middle itself
        if list[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif list[mid] > x:
            return BinarSearch(list, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return BinarSearch(list, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

def main():
    '''Main function to take input and display the output'''
    s = input('Enter the list of elements: ')
    element = int(input('Enter the element to be searched: '))
    list = s.split() #Split function returns a list of elements
    n = len(list)
    for i in range(n):#For Loop to convert string to integers
        list[i] = int(list[i])
    pos = BinarSearch(list,0,n-1,element)
    if pos == -1:# If element is not present raise an exception
        try:
            raise MyError(n)
        except MyError as error:
            print('Element '+str(element)+' not found')
    else:
        print('Element found at index '+str(pos)) #If element is present display its position


main()



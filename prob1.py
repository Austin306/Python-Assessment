class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))


def BinarySearch(list,element):
    '''This function performs binary search and returns the position of element if it is present otherwise
        it returns -1'''
    lower = 0
    upper = len(list)-1
    pos = -1
    while (lower <= upper):
        mid = (lower + upper)//2
        if list[mid] == element:
            pos = mid
            break
        elif element > list[mid]:
            lower = mid +1
        else:
            upper = mid + 1
    return pos

def main():
    '''Main function to take input and display the output'''
    s = input('Enter the list of elements: ')
    element = int(input('Enter the element to be searched: '))
    list = s.split() #Split function returns a list of elements
    n = len(list)
    for i in range(n):#For Loop to convert string to integers
        list[i] = int(list[i])
    pos = BinarySearch(list,element)
    if pos == -1:# If element is not present raise an exception
        try:
            raise MyError(n)
        except MyError as error:
            print('Element '+str(element)+' not found')
    else:
        print('Element found at index '+str(pos)) #If element is present display its position


main()



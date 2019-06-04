def comparator( tupleElem ) :
    '''This function returns last element of tuple'''
    return tupleElem[1]
def main():
    '''This function takes the tuple as input and sorts it'''
    final_list = []
    lines = input('Enter the list of tuples separated by , : ')
    for tup in lines.split('),('):#This For Loop is used to obtian the tuble from entered list
        tup = tup.replace(')','').replace('(','')
        final_list.append(tuple(tup.split(',')))
    print('The Entered List of tuples is: ')
    print(final_list)#Display unsorted list
    final_list.sort(key=lambda elem: elem[1])#Sort the tuples based on last element
    print('The Sorted List of Tuples is')
    print(final_list)
main()

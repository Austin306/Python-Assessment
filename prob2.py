def comparator( tupleElem ) :
    return tupleElem[1]
def main():
    final_list = []
    lines = input('Enter the list of tuples separated by , : ')
    for tup in lines.split('),('):
        tup = tup.replace(')','').replace('(','')
        final_list.append(tuple(tup.split(',')))
    print('The Entered List of tuples is: ')
    print(final_list)
    final_list.sort(key=lambda elem: elem[1])
    print('The Sorted List of Tuples is')
    print(final_list)
main()

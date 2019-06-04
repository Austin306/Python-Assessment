def main():
    '''Main function to sort list according to new lex order'''
    string = input('Enter the list of strings separated by space: ')
    lex = input('Enter the lex order')#New lex order
    list = string.split()#Spilt function returns list
    sorted_list = sorted(list, key = lambda word: [lex.index(c) for c in word])#Use lambda to sort list according to new lex order
    print(sorted_list)

main()

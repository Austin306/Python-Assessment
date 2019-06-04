def main():
    string = input('Enter the list of strings separated by space: ')
    lex = input('Enter the lex order')
    list = string.split()
    sorted_list = sorted(list, key = lambda word: [lex.index(c) for c in word])
    print(sorted_list)

main()

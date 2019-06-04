ConnectionsFormed=[] #Global Connection
def findConnections(name1, name2):
    if len(ConnectionsFormed)==0:
        connect=[name1,name2]
        ConnectionsFormed.append(connect)
    else:
        found=1
        for i in ConnectionsFormed:
            if name1 in i :
                i.append(name2)
                found=1
                return
            elif name2 in i:
                i.append(name1)
                found=1
                return
            else:
                found=0
        if found==0:
            connect=[name1,name2]
            ConnectionsFormed.append(connect)

def printConnections():
    for i in ConnectionsFormed:
        print(i)
def queryConnections(name1, name2):
    for i in ConnectionsFormed:
        if (name1 in i) and (name2 in i):
           print("Yes")
           return

    print("No")


n_entries=int(input("Enter number of Entries to be filled: "))#Enter the number of entries
for i in range(n_entries):#For loop to group the entries
    print("enter entries")
    entries=list(input().split(' '))
    findConnections(entries[0],entries[1])
    entries.clear()
printConnections()
print(len(ConnectionsFormed))

n_queries=int(input("Enter number of Entries to be querried"))
for i in range(n_queries):
    print("Enter queries")
    entries=list(input().split(' '))
    queryConnections(entries[0],entries[1])

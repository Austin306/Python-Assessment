ConnectionsFormed=[] #Global Connection
def findConnections(name1, name2):
    if len(ConnectionsFormed)==0:
        connect=[name1,name2]
        ConnectionsFormed.append(connect)#If a new connection directly append it to Global connection
    else:
        found=1
        for i in ConnectionsFormed:#If connection is present 
            if name1 in i :#Check if name1 is already present and append the name2 to already present connection 
                i.append(name2)
                found=1
                return
            elif name2 in i:#Check if name2 is already present then add name1 as a new connection to already existing list
                i.append(name1)
                found=1
                return
            else:
                found=0
        if found==0:
            connect=[name1,name2] #If names dont exist create a new connection
            ConnectionsFormed.append(connect)

def printConnections():
    '''Function to print the connections'''
    for i in ConnectionsFormed:
        print(i)
def queryConnections(name1, name2):
    '''Function to check if both the names are interlinked'''
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
    entries.clear()#refresh the entries 
printConnections()
print(len(ConnectionsFormed))

n_queries=int(input("Enter number of Entries to be querried"))
for i in range(n_queries):
    print("Enter queries")
    entries=list(input().split(' '))
    queryConnections(entries[0],entries[1])

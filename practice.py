q= list()
index=0
# For inserting element
def enqueue(q,element):
    q.append(element)
#function to check where queue is empty
def isEmpty(q):
    if len(q)==0:
        return True
    else:
        return False
#Remove element from queue
def dequeue(q):
    if not (isEmpty(q)):
        return q.pop(0)
    else:
        return " Queue is empty"
#check size of Queue
def size(q):
    return len(q)
#display element in queue
def display(q):
    if isEmpty(q):
        return True
    else:
        for element in q:
            print (element)
while(True):
    print("Menu")
    print(" 1.Enqueue \n 2.Dequeue \n 3.Display \n 4.Size \n 5.Exit")
    choice =int(input("Enter Your Choice"))
    if choice==1:
        index+=1
        enqueue(q,index)
        print("Element Added")
        continue
    elif choice==2:
        removeelement = dequeue(q)
        print("Element Removed :",removeelement)
        continue
    elif choice ==3:
        print("Element in queue are")
        display(q)
        continue
    elif choice == 4:
        print("Size of Queue is ", size(q))
        continue
    elif choice ==5:
        break
    else:
        print("Wrong Choice")


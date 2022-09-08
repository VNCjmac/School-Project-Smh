dest=input("Where would you like to go?: ")
itemint=int(input("How many items are you going to pack?: "))
taskint=int(input("How many tasks do you need to complete preparation?: "))

items=[]
tasks=[]

for i in range(itemint):
    items.append(input("Enter item {}/{}: ".format(i+1, itemint)))
print("Item capacity full. Moving onto tasks.")
for i in range(taskint):
    tasks.append(input("Enter task {}/{}: ".format(i+1, taskint)))
print("Task capactiy full\nHoliday to {} was successfully booked.".format(dest))
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime

ToDoList = []

def addNewItems():
    global ToDoList
    taskname = input("Please enter a new task: ")
    if checkItemExists(taskname):
        print("Task already exists! Please select options again.")
        return
    date = input("Please enter the date in format: yyyy/mm/dd HH:MM:SS: ")
    current_time = datetime.now()
    task_date = datetime.strptime(date, "%Y/%m/%d %H:%M:%S")
    
    if task_date < current_time:
        print("Time entered is in the past! Select the options again.")
    else:
        item_text = task_date.strftime("%Y/%m/%d %H:%M:%S") + ' - ' + taskname
        ToDoList.append((task_date, taskname))
        print("Task added successfully.")
    ToDoList.sort(key=takeSecond)

def checkItemExists(taskname):
    global ToDoList
    for item in ToDoList:
        if taskname == item[1]:
            return True
    return False
    
def takeSecond(element):
    return (element[0], element[1]) 

def printListItems():
    print("To Do List:")
    for i, (date, taskname) in enumerate(ToDoList):
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        print("{}. {} - {}".format(i, formatted_date, taskname))

def removeListItems():
    remove = int(input("Please enter task position: "))
    if remove < 0 or remove >= len(ToDoList):
        print("Invalid task position. Please select options again.")
    else:
        del ToDoList[remove]
        print("Task removed successfully.")

while True:
    print('''
    1 - Enter a new To Do task
    2 - Print the list of all To Do tasks
    3 - Remove a To Do task
    4 - Exit the program
    ''')

    option = int(input("Please enter an option (1/2/3/4): "))

    if option == 1:
        addNewItems()
    elif option == 2:
        printListItems()
    elif option == 3: 
        removeListItems()
    elif option == 4:
        print("End of program.")
        break
    else: 
        print("Invalid option. Please try again.")


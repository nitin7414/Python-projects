
task_time = {
    'Bath' : '7:00-7:25',
    'Breakfast':'7:30-8:00',
    'Python' : '8:10-12:30',
    'lunch' : '12:40-1:20'
}

print(
    '\n *********To-Do-List*********'
    '\n 1.To show the list.'
    '\n 2.To add something to list.'
    '\n 3.To remove something dompleted'
    '\n 4.To exit ! '
)

def add_task():
    add = input('Enter the task: ').strip()
    add_time = input('Enter the time: ').strip()
    task_time[add] = add_time
    print(f'New task {add} has been scheduled for {add_time} ')

def done():
    remove_item = input('Enet the task that has been completed: ').capitalize()
    if remove_item in task_time.keys():
     task_time.pop(remove_item)
     print(f'✅ {remove_item} has been assigned as removed..' )
    else:
        print(f'The {remove_item} is not in the list')

while True:
    check = int(input('Enter the s.no.: '))
    if check==1:
        for i,v in enumerate(task_time.items(), start=1):
            print(i,v)
    elif check==2:
        add_task()
        new_task = input('Do you want to add another task? ')
        if new_task=='y':
            add_task()
        elif new_task=='n':
            continue
    elif check==3:
        done()
    elif check==4:
        print('Bbyeee! 👋.......')
        break


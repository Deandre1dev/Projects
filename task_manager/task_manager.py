#=====importing libraries===========

'''This is the section where you will import libraries'''
usernames = []
passwords = []
with open("user.txt","r") as file:

# #====Login Section====
    
    for lines in file:
        temp=lines.strip()
        temp=lines.split(", ")
        print(temp)

    usernames.append(temp[0])
    passwords.append(temp[1])

    user_names = input("Enter your username : ")
    pass_words = input("Enter your password : ")

    print(usernames)
    print(passwords)

#If the users password and username already exists they are logged in.
#If not they are prompted to add a new username and password that does not exist in the txt file.

if user_names in usernames and pass_words in passwords:
    file.close()

else:
        while user_names in usernames:
                print("This username already exist")
                user_names = input("Enter your username : ")
                usernames.append(temp[0])

        while pass_words in passwords:
                print("This password already exist")
                pass_words = input("Enter your password : ")
                passwords.append(temp[1])
            

        else:
                file = open("user.txt","a")
                file.write(f"\n{user_names}, {pass_words}")

                file.close()

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    #This menu activates if the admin user is logged in.
    if user_names == "admin" and pass_words == "adm1n":
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        s - Statistics
        : ''').lower()

    #This menu is displayed to regular users.

    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()



    if menu == 'r':
        pass
    
    #The admin user is only allowed to add a new user
    # if the user is not admin access is denied

        if user_names != "admin" and pass_words != "adm1n":
            print("Access Denied!")

        elif user_names == "admin" and pass_words == "adm1n":
            new_names = input("Enter your username : ")
            new_pass_words = input("Enter your password : ")
            confirm_pass_word = input("Confirm your password : ")

            while new_pass_words == confirm_pass_word:
                file = open("user.txt","a")
                file.write(f"\n{new_names}, {new_pass_words}")

                file.close()
            
            
            else:
                while new_pass_words != confirm_pass_word:
                        print("The password does not match")
                        confirm_pass_word = input("Confirm your password : ")
                else:
                    file = open("user.txt","a")
                    file.write(f"\n{new_names}, {new_pass_words}")
                
        file.close
                
    #User can add a task     
    
    elif menu == 'a':
        pass

        user = input("Enter username of the person the task is assinged to : ")
        title_of_task = input("Enter the title of the task : ")
        task_description = input("Enter task description : ")
        due_date = input("Enter the due date for the task (e.g 1 Jan 2000): ")
        start_date = input("Enter current date in format (e.g 1 Jan 2000): ")
        task_comp = ("No")

        file_task = open("tasks.txt","a+")
        file_task.write(f"\n{user}, {title_of_task}, {task_description}, {start_date}, {due_date}, {task_comp}")

        file_task.close()

    #User can veiw all tasks

    elif menu == 'va':
        pass
       
        file_task = open("tasks.txt","r")
        sentence = file_task.readlines()
    
        for line in sentence:
            temp = line.strip()
            temp = temp.split(", ")
        
            print("Task:\t\t\t"+temp[1])
            print("Assigned to:\t\t"+temp[0])
            print("Date assigned:\t\t"+temp[3])
            print("Due date:\t\t"+temp[4])
            print("Task complete?\t\t"+temp[5])
            print("task description:\n "+temp[2])
        
                
        
        file_task.close()

    #User can veiw their tasks
        
    elif menu == 'vm':
        pass
        
        file_task = open("tasks.txt","r")
        lines = file_task.readlines()

        for line in lines :
            temp = line.strip()
            temp = temp.split(", ")
            if user_names in line:

                print("Task:\t\t\t"+temp[1])
                print("Assigned to:\t\t"+temp[0])
                print("Date assigned:\t\t"+temp[3])
                print("Due date:\t\t"+temp[4])
                print("Task complete?\t\t"+temp[5])
                print("task description:\n "+temp[2])
            

        file_task.close()

    #Admin user can veiw the statistics

    elif menu == 's':
        pass
    
        print("Statistics")
        with open("user.txt","r") as num_users:
              users = len(num_users.readlines()) 
              print("The total amount of users are :" +(str(users)))
              num_users.close()

        with open("tasks.txt","r") as num_tasks:
              tasks = len(num_tasks.readlines())
              print("The total amount of tasks are :" +(str(tasks)))
              num_tasks.close()



    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
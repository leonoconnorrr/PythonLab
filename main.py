while True:
    print("1. Show ")
    print("2. Add ")
    print("3. Update ")
    print("4. Delete ")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        with open("data.txt", "r") as file:
            for line in file:
                if line.strip():
                    print(line.strip())

    elif choice == "2":
        user_id = input("ID: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone Number: ")
        
        with open("data.txt", "r") as file:
            lines = file.readlines()
            
        new_id = 1
        for line in lines:
            if line.strip():
                new_id = new_id + 1
        
        with open("data.txt", "a") as file:
            file.write(str(new_id) + "," + first_name + "," + last_name + "," + email + "," + phone + "\n")
        print("Done")

    elif choice == "3":
        user_id = input("Enter ID to update: ")
        
        with open("data.txt", "r") as file:
            lines = file.readlines()
            
        with open("data.txt", "w") as file:
            for line in lines:
                if line.strip():
                    data = line.strip().split(",")
                    if data[0] == user_id:
                        print("Updating")
                        new_first = input("New First Name: ")
                        new_last = input("New Last Name: ")
                        new_email = input("New Email: ")
                        new_phone = input("New Phone Number: ")
                        a = user_id + "," + new_first + "," + new_last + "," + new_email + "," + new_phone + "\n"
                        file.write(a)
                        print("Done")
                    else:
                        file.write(line)

    elif choice == "4":
        user_id = input("Enter ID to delete: ")
        
        with open("data.txt", "r") as file:
            lines = file.readlines()
            
        with open("data.txt", "w") as file:
            new_id = 1
            for line in lines:
                if line.strip():
                    data = line.strip().split(",")
                    if data[0] != user_id:
                        file.write(str(new_id) + "," + data[1] + "," + data[2] + "," + data[3] + "," + data[4] + "\n")
                        new_id = new_id + 1
        print("Done")

    elif choice == "5":
        break

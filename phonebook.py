contacts = {}
while True:
    print("\n 1.Add contact:")
    print("2.remove contact:")
    print("3.Edit contact:")
    print("4.Search contact:")
    print("5.View Contact:")
    print("6.quit")

    choice = input("Enter Your Choice:")

    if choice == "1":
      name = input("Enter Name :")
      number = int(input("Enter number :"))
      contacts[name] = number
      print("contact added Successfully")

    elif choice == "2":
       name = input("Enter name:")
       if name in contacts:
         name.pop["name"]
         print("Contact Deleted!")
       else:
          print("Contact Not Found")

    elif choice == "3":
       name = input("Enter name to edit:")
       if name in contacts:
          phone = int(input("Enter new number:"))
          contacts[name] = phone
          print("Contact Updated")
       else:
          print("Contact Not Found")

    elif choice == "4":
       name = input("Enter Name to Search:")
       if name in contacts :
          print("phone:",contacts[name])
       else:
          print("Contact Not Found")
          
    elif choice =="5":
          print("\nContacts:")

          for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "6":
          print("Have a Nice Time")
          break

    else:
          print("Invalid Choice")
       

        

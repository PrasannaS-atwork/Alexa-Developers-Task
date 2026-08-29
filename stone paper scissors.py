import random
i=0
userscore=0
computerscore=0
print("HELLOOO......GIVE CHOICE IN RESPECTIVE CASE SHOWN BECAUSE IT IS CASE-SENSITIVE")
while i==0:
    print("stone\npaper\nscissors\nExit")
    choiceu=input("Enter your choice: ")
    L=["stone","paper","scissors"]
    num=random.randint(0,2)
    choicec=L[num]
    print()
    while True:
        if choiceu=="EXIT":
            i=1
            break
        elif choiceu==choicec:
            print("The user choice and computer choice are same - ",choiceu)
            print("It is draw")
            print()
            print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
            print()
            break
        elif choiceu=="stone":
            if choicec=="paper":
                print("The user's choice is ",choiceu," and computer choice is ",choicec)
                print("The winner is COMPUTER")
                computerscore+=1
                print()
                print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
                print()
                break
            else:
                print("The user's choice is ",choiceu," and computer choice is ",choicec)
                print("The winner is USER")
                print()
                userscore+=1
                print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
                print()
                break
        elif choiceu=="paper":
            if choicec=="stone":
                print("The user's choice is ",choiceu," and computer choice is ",choicec)
                print("The winner is USER ")
                userscore+=1
                print()
                print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
                print()
                break
            else:
                print("The user's choice is ",choiceu," and computer choice is ",choicec)
                print("The winner is COMPUTER")
                computerscore+=1
                print()
                print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
                print()
                break
        elif choiceu=="scissors":
            if choicec=="stone":
                print("The user's choice is ",choiceu," and computer choice is ",choicec)
                print("The winner is COMPUTER")
                computerscore+=1
                print()
                print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
                print()
                break
            else:
                print("The user's choice is ",choiceu," and computer choice is ",choicec)
                print("The winner is USER ")
                userscore+=1
                print()
                print("THE SCORES:\nUSER-",userscore,"\nCOMPUTER-",computerscore)
                print()
                break
        else:
            print("ENTER VALID OPTION")
            print()
            break
        
            
            
            
        

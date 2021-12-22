import csv

participants = []
exitCheck = False

def signUp(participants):
    slot = 0
    name = ""
    print("Sign up participant\n---------------")
    while True:
        slot = int(input("Slot for participant? "))
        name = str(input("Name of participant? "))
        if participants[(slot - 1)] == None:
            participants[(slot - 1)] = name
            print("Participant added. Returning to main menu.")
            break
        else:
            print("Slot occupied. Choose another.")

def cancelSignUp(participants):
    slot = 0
    name = ""
    print("Remove participant\n---------------")
    while True:
        slot = int(input("Slot for participant? "))
        name = str(input("Name of participant? "))
        if participants[(slot - 1)] != None:
            if participants[(slot - 1)] == name:
                participants[(slot - 1)] = None
                print("Participant removed. Returning to main menu.")
                break
            else:
                print("Name not found in slot " + str(slot) + ". Try again.")
        else:
            print("Slot not occupied. Try again.")

def viewParticipants(participants):
    for i in range(len(participants)):
        print(str(i + 1) + ": " + str(participants[i]))

# Main
userInput = input("How many participants?\n")
userInput = userInput.strip()
userInput = int(userInput)
participants = [None] * userInput
print("list size = " + str(len(participants)))       

while exitCheck == False:
    print("\nMain Menu\n---------")
    print("1. Sign Up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. Save")
    print("5. Exit")
    userInput = input("Enter the number for desired selection: ")
    if userInput == "1":
        signUp(participants)
    elif userInput == "2":
        cancelSignUp(participants)
    elif userInput == "3":
        print("\nParticipants:\n----------")
        viewParticipants(participants)
    elif userInput == "4":
        "\n".join(participants)
        Header = ["Name"]
        with open('participants.csv', 'w', newline = '') as f:
            write = csv.writer(f)
            write.writerow(Header)
            for i in participants:
                write.writerow([i])
            print("Exported participants list")
    elif userInput == "5":
        print("Exiting will lose any unsaved data. Continue (Y/N)? ")
        userInput = str(input()).strip().upper()[:1]
        if userInput == "Y":
            exitCheck = True
    else:
        print("Input not recognized\n")
